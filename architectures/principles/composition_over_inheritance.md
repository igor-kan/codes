# Composition over Inheritance

Prefer assembling behavior from collaborating objects over deriving behavior
through class hierarchies.

## Why

- Inheritance is the tightest coupling: subclasses depend on superclass
  internals and cannot change at runtime.
- Deep hierarchies are brittle (fragile base class) and hard to reason about.
- Multiple inheritance / mixins create diamond problems.

## Example

```python
# Inheritance: a Logger that is also a Retrying thing that is also a Thing...
class RetryingHttpClient(HttpClient): ...

# Composition: independent, swappable strategies
class HttpClient:
    def __init__(self, transport, retry_policy, serializer):
        self._transport = transport
        self._retry = retry_policy
        self._serializer = serializer
```

## When inheritance is fine

- True "is-a" with a stable, well-designed base and no behavior surprises.
- Framework extension points designed for it (e.g. React `Component`).

Related: Strategy Pattern, Delegation, Dependency Inversion.
