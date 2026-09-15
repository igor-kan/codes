# Flux

A unidirectional data flow for UIs.

```
Action -> Dispatcher -> Store -> View
  ^                                |
  +------------ user ------------- +
```

- **Action:** plain object describing intent.
- **Dispatcher:** single hub that routes actions to stores.
- **Store:** holds state and business logic; emits change events.
- **View:** renders from the store and dispatches new actions.

## Why

Predictable state transitions, easier debugging, no two-way binding loops.

Related: Redux, CQRS, Event Sourcing.
