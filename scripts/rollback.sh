#!/bin/bash
# ============================================
# rollback.sh — Rollback to a previous Docker image
# Usage: ./rollback.sh <image-tag>
# Example: ./rollback.sh sha-abc123
# ============================================

set -euo pipefail

IMAGE_TAG="${1:-}"
REPO_OWNER="${GITHUB_REPOSITORY_OWNER:-prasanm1423}"
NAMESPACE="devops-hello"
DEPLOYMENT="book-catalogue"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info()  { echo -e "${GREEN}[INFO]${NC} $*"; }
log_warn()  { echo -e "${YELLOW}[WARN]${NC} $*"; }
log_error() { echo -e "${RED}[ERROR]${NC} $*"; exit 1; }

if [[ -z "$IMAGE_TAG" ]]; then
    log_error "Image tag not specified. Usage: $0 <image-tag>"
fi

IMAGE="ghcr.io/${REPO_OWNER}/devops-hello:${IMAGE_TAG}"

log_warn "Initiating rollback to: ${IMAGE}"
log_warn "Namespace: ${NAMESPACE}, Deployment: ${DEPLOYMENT}"
echo ""

# Force rollout restart after image change
log_info "Setting image on deployment..."
kubectl set image deployment/"${DEPLOYMENT}" "${DEPLOYMENT}=${IMAGE}" \
    --namespace="${NAMESPACE}" || log_error "Failed to set image."

log_info "Waiting for rollout (timeout: 5 minutes)..."
kubectl rollout status deployment/"${DEPLOYMENT}" \
    --namespace="${NAMESPACE}" \
    --timeout=300s || log_error "Rollout failed!"

log_info "Verifying pod health..."
READY=$(kubectl get pods -l app="${DEPLOYMENT}" \
    --namespace="${NAMESPACE}" \
    -o jsonpath='{range .items[*]}{.status.containerStatuses[0].ready}{end}' 2>/dev/null || echo "false")

if [[ "${READY}" == "true" ]]; then
    log_info "Rollback to ${IMAGE} completed successfully. ✓"
else
    log_warn "Pod readiness check returned: ${READY}. Manual inspection may be required."
    kubectl get pods -l app="${DEPLOYMENT}" --namespace="${NAMESPACE}" -o wide
fi

echo ""
log_info "=========================================="
log_info "Rollback Summary"
log_info "=========================================="
log_info "Target Image : ${IMAGE}"
log_info "Namespace    : ${NAMESPACE}"
log_info "Deployment   : ${DEPLOYMENT}"
log_info "Status       : Completed"
log_info "=========================================="
