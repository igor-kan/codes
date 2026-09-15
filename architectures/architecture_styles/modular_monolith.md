# Modular Monolith

One deployable, but internally partitioned into well-bounded modules with
explicit interfaces.

## Practices

- Enforce module boundaries in code (packages, build rules, ArchUnit tests).
- Modules communicate via in-process interfaces or events, not shared tables.
- Each module owns its schema/slice of the database.

## Why

- Avoids premature distributed complexity.
- Eases a later extraction to services ("extract, don't rewrite").

Related: Monolith, Microservices, DDD Bounded Contexts.
