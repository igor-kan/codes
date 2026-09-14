# Law of Demeter (Principle of Least Knowledge)

A module should talk only to its immediate collaborators, not to the internals
of objects it obtains from them.

```python
# Violates: reaches through order -> customer -> address -> city
city = order.customer.address.city

# Respects: ask the object that owns the knowledge
city = order.shipping_city()
```

## Why it matters

- Reduces coupling to object graphs and their internal structure.
- Makes change localized: `Address` can evolve without touching callers.
- Improves testability (fewer stubs per test).

## Recognizing "train wrecks"

`a.b().c().d()` in application code is a smell; delegation methods or moving the
behavior closer to the data usually fixes it.

**Trade-off:** over-applying it produces wrappers that just forward calls.
Apply it to *structural* knowledge, not to fluent builders or value access.

Related: Tell Don't Ask, Encapsulation, Coupling/Cohesion.
