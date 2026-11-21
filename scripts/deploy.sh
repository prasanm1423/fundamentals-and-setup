#!/bin/bash
# ============================================
# deploy.sh — Automated Deployment Script
# Supports: staging | production | rollback
# Usage: ./deploy.sh <environment> [--image <tag>] [--rollback]
# ============================================

set -euo pipefail

ENVIRONMENT="${1:-}"
IMAGE_TAG="${2:-}"
ACTION="${3:-}"
REPO_OWNER="${GITHUB_REPOSITORY_OWNER:-prasanm1423}"
NAMESPACE="devops-hello"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info()  { echo -e "${GREEN}[INFO]${NC} $*"; }
log_warn()  { echo -e "${YELLOW}[WARN]${NC} $*"; }
log_error() { echo -e "${RED}[ERROR]${NC} $*"; exit 1; }

usage() {
    echo "Usage: $0 <staging|production|rollback> [--image <tag>] [--rollback]"
    echo ""
    echo "Examples:"
    echo "  $0 staging                                  # Deploy latest commit to staging"
    echo "  $0 production --image sha-abc123             # Deploy specific image to production"
    echo "  $0 rollback --image sha-def456               # Rollback to previous image"
    exit 1
}

if [[ -z "$ENVIRONMENT" ]]; then
    log_error "Environment not specified. Use: staging or production"
fi

case "$ENVIRONMENT" in
    staging|production|rollback) ;;
    *) log_error "Invalid environment: $ENVIRONMENT. Use 'staging' or 'production'.";;
esac

while [[ $# -gt 0 ]]; do
    case $1 in
        --image)
            IMAGE_TAG="$2"
            shift 2
            ;;
        --rollback)
            ACTION="rollback"
            shift
            ;;
        *)
            log_error "Unknown flag: $1"
            ;;
    esac
done

if [[ -z "$IMAGE_TAG" ]]; then
    IMAGE_TAG="sha-${GITHUB_SHA:-local}"
fi

DEPLOY_IMAGE="ghcr.io/${REPO_OWNER}/devops-hello:${IMAGE_TAG}"
KUBE_MANIFEST="k8s/deployment.yaml"

log_info "=========================================="
log_info "Deployment Configuration"
log_info "=========================================="
log_info "Environment : ${ENVIRONMENT^^}"
log_info "Image       : ${DEPLOY_IMAGE}"
log_info "Namespace   : ${NAMESPACE}"
log_info "Manifest    : ${KUBE_MANIFEST}"
log_info "=========================================="
echo ""

pre_deploy_check() {
    log_info "Running pre-deployment checks..."
    if command -v kubectl &>/dev/null && [[ -f "${KUBECONFIG:-$HOME/.kube/config}" ]]; then
        if kubectl get namespace "${NAMESPACE}" &>/dev/null; then
            log_info "Namespace '${NAMESPACE}' exists."
        else
            log_warn "Namespace '${NAMESPACE}' not found. Creating..."
            kubectl create namespace "${NAMESPACE}"
        fi
    else
        log_warn "kubectl not found or KUBECONFIG not set. Simulating deployment."
    fi
    log_info "Pre-deployment checks passed."
}

deploy() {
    local env_label=$1
    log_info "Deploying to ${env_label}..."

    sed -i.bak "s|image: devops-hello:latest|image: ${DEPLOY_IMAGE}|g" "${KUBE_MANIFEST}"
    sed -i.bak "s|env: prod|env: ${env_label}|g" "${KUBE_MANIFEST}"

    log_info "Applying Kubernetes manifests..."
    kubectl apply -f "${KUBE_MANIFEST}" --namespace="${NAMESPACE}" || {
        log_error "Failed to apply Kubernetes manifests."
    }

    log_info "Waiting for rollout to complete (timeout: 5 minutes)..."
    kubectl rollout status deployment/book-catalogue \
        --namespace="${NAMESPACE}" \
        --timeout=300s || {
        log_error "Rollout failed. Initiating rollback..."
        rollback
    }

    log_info "Rollout successful!"
}

rollback() {
    log_warn "Initiating rollback to image: ${DEPLOY_IMAGE}"
    kubectl set image deployment/book-catalogue book-catalogue="${DEPLOY_IMAGE}" \
        --namespace="${NAMESPACE}" || {
        log_error "Rollback failed!"
    }
    kubectl rollout status deployment/book-catalogue \
        --namespace="${NAMESPACE}" \
        --timeout=300s || {
        log_error "Rollback rollout failed!"
    }
    log_info "Rollback to ${IMAGE_TAG} completed successfully."
}

post_deploy_verify() {
    local env_label=$1
    log_info "Running post-deployment verification..."

    if command -v kubectl &>/dev/null; then
        local pod_status
        pod_status=$(kubectl get pods -l app=book-catalogue \
            --namespace="${NAMESPACE}" \
            -o jsonpath='{.items[0].status.phase}' 2>/dev/null || echo "UNKNOWN")

        if [[ "${pod_status}" == "Running" ]]; then
            log_info "Pod status: Running ✓"
        else
            log_warn "Pod status: ${pod_status}. Checking events..."
            kubectl describe pods -l app=book-catalogue \
                --namespace="${NAMESPACE}" | tail -20
        fi
    else
        log_warn "kubectl not available — skipping live pod verification."
    fi

    log_info "Post-deployment verification complete."
}

main() {
    case "${ENVIRONMENT}" in
        staging)
            pre_deploy_check
            deploy "staging"
            post_deploy_verify "staging"
            ;;
        production)
            pre_deploy_check
            deploy "production"
            post_deploy_verify "production"
            ;;
        rollback)
            rollback
            ;;
    esac

    log_info "=========================================="
    log_info "Deployment complete!"
    log_info "Image: ${DEPLOY_IMAGE}"
    log_info "=========================================="
}

main
