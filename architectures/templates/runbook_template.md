# Runbook: <Alert / Service>

- **Alert:** `HighErrorRate`
- **Severity:** SEV-2
- **Owner:** Platform Team
- **Escalation:** #oncall-platform

## Symptoms

What the operator observes (dashboards, alert text, customer reports).

## Impact

User-visible effect, blast radius, and SLO at risk.

## Diagnosis

1. Open the [API dashboard](https://grafana.example.com/d/api-overview).
2. Check error budget burn and recent deploys (`git log`, CD history).
3. Inspect logs: `kubectl -n prod logs deploy/api --since=15m | grep -i error`.
4. Check dependencies: database connections, queue depth, third-party status.

## Mitigation

- **If caused by a bad deploy:** roll back — `kubectl rollout undo deploy/api`.
- **If dependency is down:** enable the circuit breaker / failover flag.
- **If saturated:** scale out — `kubectl scale deploy/api --replicas=10`.

## Verification

- Error rate returns to baseline for 10 minutes.
- No new alerts; synthetic checks green.

## Follow-up

- File an incident review within 3 business days.
- Add a regression test or alert; update this runbook.
