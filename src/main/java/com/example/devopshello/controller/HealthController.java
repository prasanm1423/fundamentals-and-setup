package com.example.devopshello.controller;

import org.springframework.boot.actuate.health.Health;
import org.springframework.boot.actuate.health.HealthIndicator;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.time.Instant;
import java.util.LinkedHashMap;
import java.util.Map;

/**
 * Custom application health indicator exposed at /api/health.
 * Complements Spring Boot Actuator's built-in /actuator/health endpoint.
 */
@RestController
public class HealthController implements HealthIndicator {

    private volatile String status = "UP";
    private volatile Map<String, Object> details = new LinkedHashMap<>();

    @GetMapping("/api/health")
    public ResponseEntity<Map<String, Object>> getHealth() {
        Map<String, Object> response = new LinkedHashMap<>();
        response.put("status", status);
        response.put("timestamp", Instant.now().toString());
        response.putAll(details);
        return ResponseEntity.ok(response);
    }

    /** Called by tests or deployment scripts to simulate failures */
    public void setUnhealthy(boolean unhealthy) {
        this.status = unhealthy ? "DOWN" : "UP";
        this.details.put("lastCheck", Instant.now().toString());
    }

    @Override
    public Health health() {
        return Health.up()
                .withDetail("application", "devops-hello")
                .withDetail("timestamp", Instant.now().toString())
                .build();
    }
}
