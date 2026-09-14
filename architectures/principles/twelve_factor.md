# The Twelve-Factor App

Methodology for building portable, operationally sound services.

1. **Codebase** — one repo per app, many deploys.
2. **Dependencies** — declare and isolate explicitly.
3. **Config** — store in the environment, not the code.
4. **Backing services** — treat as attached resources, swappable by config.
5. **Build, release, run** — strict separation; immutable releases.
6. **Processes** — stateless; share-nothing; persist state in backing services.
7. **Port binding** — self-contained, export services via a port.
8. **Concurrency** — scale out via the process model.
9. **Disposability** — fast startup, graceful shutdown on `SIGTERM`.
10. **Dev/prod parity** — keep environments as similar as possible.
11. **Logs** — treat as event streams to stdout; do not manage files.
12. **Admin processes** — run as one-off processes (migrations, consoles).

## Beyond twelve-factor

- **API first**, **telemetry as a first-class concern**, **auth by default**.
- Container and orchestrator conventions (health probes, resource limits).

Related: Cloud-Native, DevOps, Configuration Management.
