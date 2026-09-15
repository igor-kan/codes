# Least Privilege

Grant the minimum permissions needed, for the minimum time, to do the job.

## Applications

- Fine-grained IAM roles and per-service identities.
- Short-lived credentials (OIDC, STS) over static keys.
- Just-in-time elevation with approval and expiry.
- Read-only defaults; explicit grants for writes.
- Separate build, deploy, and runtime identities.

## Pitfalls

- Wildcard permissions accumulated over time.
- Long-lived shared credentials.
- Over-broad service accounts and containers running as root.

Related: Zero Trust, RBAC, Secrets Management.
