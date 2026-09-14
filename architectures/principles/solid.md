# SOLID Principles

| Principle | Statement | Smell when violated |
|:---|:---|:---|
| **S**ingle Responsibility | A module has one reason to change | God classes, "Manager" types |
| **O**pen/Closed | Open for extension, closed for modification | Growing `switch` on type tags |
| **L**iskov Substitution | Subtypes are usable wherever the base type is | Overrides that throw or narrow |
| **I**nterface Segregation | Many small interfaces over one fat one | Empty/throwaway implementations |
| **D**ependency Inversion | Depend on abstractions, not concretions | Direct `new` of infrastructure in domain |

## Example: Dependency Inversion

```python
class Clock(Protocol):
    def now(self) -> datetime: ...

class OrderService:
    def __init__(self, clock: Clock, repo: OrderRepository) -> None:
        self._clock = clock
        self._repo = repo
```

The domain depends on `Clock`/`OrderRepository` interfaces; infrastructure
provides adapters. This keeps the core testable without a database.

Related: Clean Architecture, Hexagonal, Composition over Inheritance.
