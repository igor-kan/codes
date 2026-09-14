# Architectures Reference Library

Design patterns, concurrency primitives, and distributed systems patterns across multiple languages.

## Pattern Coverage

### Gang of Four Design Patterns

| Pattern | Category | C++ | Go | Java | Python |
|---------|----------|-----|-----|------|--------|
| Abstract Factory | Creational | ✓ | ✓ | | ✓ |
| Builder | Creational | ✓ | ✓ | ✓ | ✓ |
| Factory Method | Creational | ✓ | ✓ | | ✓ |
| Prototype | Creational | ✓ | ✓ | | ✓ |
| Singleton | Creational | ✓ | ✓ | | |
| Simple Factory | Creational | | ✓ | | |
| Adapter | Structural | ✓ | ✓ | | ✓ |
| Bridge | Structural | ✓ | ✓ | | ✓ |
| Composite | Structural | ✓ | ✓ | | ✓ |
| Decorator | Structural | ✓ | ✓ | | ✓ |
| Facade | Structural | ✓ | ✓ | | ✓ |
| Flyweight | Structural | ✓ | ✓ | | ✓ |
| Proxy | Structural | ✓ | ✓ | | ✓ |
| Chain of Responsibility | Behavioral | ✓ | ✓ | | ✓ |
| Command | Behavioral | ✓ | ✓ | | ✓ |
| Interpreter | Behavioral | ✓ | ✓ | | |
| Iterator | Behavioral | ✓ | ✓ | | ✓ |
| Mediator | Behavioral | ✓ | ✓ | | ✓ |
| Memento | Behavioral | ✓ | ✓ | | ✓ |
| Observer | Behavioral | ✓ | ✓ | ✓ | ✓ |
| State | Behavioral | ✓ | ✓ | | ✓ |
| Strategy | Behavioral | ✓ | ✓ | | ✓ |
| Template Method | Behavioral | ✓ | ✓ | | ✓ |
| Visitor | Behavioral | ✓ | ✓ | | ✓ |

### Python-Specific Patterns

| Pattern | Category |
|---------|----------|
| Borg (shared-state singleton) | Creational |
| Lazy Evaluation | Creational |
| Pool | Creational |
| Dependency Injection | Other |
| Chaining Method | Behavioral |
| Registry | Behavioral |
| Specification | Behavioral |
| Delegation | Fundamental |
| MVC | Structural |
| Front Controller | Structural |
| 3-Tier | Structural |
| Blackboard | Other |
| Graph Search | Other |
| HSM (Hierarchical State Machine) | Other |
| Publish-Subscribe | Behavioral |
| Catalog | Behavioral |
| Servant | Behavioral |

### Concurrency Patterns

| Pattern | Language | File |
|---------|----------|------|
| Actor Model | Go | `actor_model.go` |
| Actor System (demo) | Go | `actor_system.go` |
| Thread Pool | C++ | `thread_pool.cpp` |
| Worker Pool | Rust | `worker_pool.rs` |

### Distributed Systems Patterns

| Pattern | Language | File |
|---------|----------|------|
| Consistent Hashing Ring | Rust | `consistent_hashing.rs` |
| Circuit Breaker | Go | `circuit_breaker.go` |

### TypeScript Patterns

| Pattern | File |
|---------|------|
| Middleware Pipeline (Onion) | `middleware_pipeline.ts` |
| Repository + Unit of Work | `repository_pattern.ts` |
| |

---

## Directory Layout

```
architectures/
├── cpp_patterns/         Gang of Four — 24 patterns in classic C++
│                         (by Jakub Vojvoda, MIT)
├── go_patterns/          Gang of Four — 24 patterns with tests in Go
├── python_patterns/      Gang of Four + pythonic patterns + tests
│                         (includes lint.sh with codespell, flake8, mypy, pytest)
├── java_patterns/        Builder and Observer pattern demos
├── concurrency_patterns/ Actor models, thread/worker pools
├── distributed_patterns/ Consistent hashing, circuit breaker
└── typescript_patterns/  Middleware pipeline, repository pattern
```

---

## Testing

```bash
# Run all architecture tests
make test-architectures

# Python patterns (includes linting, typechecking, and pytest)
cd architectures/python_patterns && bash lint.sh
```