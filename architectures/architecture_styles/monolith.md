# Monolith

A single deployable containing all functionality, sharing one database.

## Pros

- Simple to develop, test, and deploy.
- No network boundaries or distributed transactions.
- Fast refactoring within one codebase.

## Cons

- Coupling grows; build/test times increase.
- Scaling is all-or-nothing.
- One bug can take down everything.

Use a **modular monolith** to keep boundaries clean until independent
deployment is truly needed.

Related: Modular Monolith, Microservices.
