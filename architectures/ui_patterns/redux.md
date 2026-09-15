# Redux

A predictable state container: a single **store**, pure **reducers**, and
immutable state transitions driven by dispatched **actions**.

```js
const reducer = (state = {}, action) =>
  action.type === "ADD" ? { ...state, items: [...state.items, action.item] } : state;
```

## Principles

1. Single source of truth.
2. State is read-only; changes are made by dispatching actions.
3. Changes are pure functions of `(state, action)`.

## Ecosystem ideas

Middleware (thunks/sagas) for effects, selectors for derived state, devtools for
time-travel debugging.

Trade-offs: boilerplate and global state pressure; use local state where it fits.

Related: Flux, CQRS, Event Sourcing.
