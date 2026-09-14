# Onion Architecture

A variant of layered design with the **domain model at the core** and all
dependencies pointing inward. Coined by Jeffrey Palermo; closely related to
Hexagonal and Clean Architecture.

```
   Domain Model
     Domain Services
       Application Services
         Infrastructure / UI / Tests
```

## Dependency rule

- Outer rings may depend on inner rings, never the reverse.
- The domain has no dependencies on frameworks, databases, or I/O.
- Interfaces (repositories, gateways) are declared in inner rings and
  implemented in outer rings.

## Comparison

| Approach | Center | Emphasis |
|:---|:---|:---|
| Onion | domain model | dependency direction |
| Hexagonal | use cases | ports and adapters |
| Clean | entities + use cases | concentric layers, stable abstractions |

All three share the same core idea: protect business logic from volatility in
frameworks and infrastructure.

Related: Hexagonal, Clean Architecture, Dependency Inversion, DDD.
