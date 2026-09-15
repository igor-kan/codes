# Health Checks

Expose liveness and readiness so orchestrators can manage instances correctly.

## Liveness

"Is the process healthy enough to keep running?" Failure triggers restart.

## Readiness

"Can this instance serve traffic now?" Failure removes it from load balancing.

## Startup

For slow-starting apps, a startup probe prevents premature restarts.

## Practices

- Keep checks cheap and dependency-light (liveness must not call a DB).
- Readiness may check critical dependencies, with timeouts.
- Add deep diagnostics on a separate, protected endpoint.

Related: Kubernetes probes, Deployment Patterns.
