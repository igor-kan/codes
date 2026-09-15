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

### Enterprise Integration Patterns (Python)

| Pattern | File |
|---------|------|
| Message Router | `enterprise_patterns/message_router.py` |
| Content-Based Router | `enterprise_patterns/content_based_router.py` |
| Splitter | `enterprise_patterns/splitter.py` |
| Aggregator | `enterprise_patterns/aggregator.py` |
| Transactional Outbox | `enterprise_patterns/outbox.py` |
| Saga (compensating transactions) | `enterprise_patterns/saga.py` |
| Idempotent Receiver | `enterprise_patterns/idempotent_receiver.py` |
| Dead Letter Channel | `enterprise_patterns/dead_letter_channel.py` |

### Domain-Driven Design Patterns (Python)

| Pattern | File |
|---------|------|
| Entity | `ddd_patterns/entity.py` |
| Value Object | `ddd_patterns/value_object.py` |
| Aggregate | `ddd_patterns/aggregate.py` |
| Repository | `ddd_patterns/repository.py` |
| Domain Event | `ddd_patterns/domain_event.py` |
| Specification | `ddd_patterns/specification.py` |
| Domain Service | `ddd_patterns/domain_service.py` |

### Cloud & Resilience Patterns

| Pattern | Format | File |
|---------|--------|------|
| Circuit Breaker | Python | `cloud_patterns/circuit_breaker.py` |
| Bulkhead | Python | `cloud_patterns/bulkhead.py` |
| Retry with Backoff + Jitter | Python | `cloud_patterns/retry_backoff.py` |
| Cache-Aside | Python | `cloud_patterns/cache_aside.py` |
| Sidecar | Doc | `cloud_patterns/sidecar.md` |
| Ambassador | Doc | `cloud_patterns/ambassador.md` |
| Strangler Fig | Doc | `cloud_patterns/strangler_fig.md` |
| Gateway Offloading | Doc | `cloud_patterns/gateway_offloading.md` |

### System Design Building Blocks

| Topic | Format | File |
|---------|--------|------|
| Token-Bucket Rate Limiter | Python | `system_design/rate_limiter.py` |
| Load Balancing Strategies | Python | `system_design/load_balancer.py` |
| LRU Cache | Python | `system_design/lru_cache.py` |
| Write-Ahead Log | Python | `system_design/write_ahead_log.py` |
| Sharding | Doc | `system_design/sharding.md` |
| CDN | Doc | `system_design/cdn.md` |
| CAP / PACELC | Doc | `system_design/cap_theorem.md` |
| Bloom Filter Guard | Doc | `system_design/bloom_filter_guard.md` |

### Principles, Clean Architecture, Templates & API Design

| Area | Files |
|---------|-------|
| Engineering principles | `principles/`: SOLID, DRY/KISS/YAGNI, separation of concerns, Law of Demeter, composition over inheritance, Twelve-Factor |
| Clean architecture | `clean_architecture/`: dependency inversion, ports & adapters, hexagonal, layered, onion |
| Design templates | `templates/`: ADR, RFC, design doc, runbook, C4 context & container (Mermaid) |
| API design | `api_design/`: REST guidelines, versioning, pagination, error handling, GraphQL vs REST |

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
├── typescript_patterns/  Middleware pipeline, repository pattern
├── enterprise_patterns/  Messaging integration patterns (router, saga, outbox, …)
├── integration_patterns/ EIP: channels, pipes/filters, translators, wire tap
├── ddd_patterns/         Entities, value objects, aggregates, repositories, events
├── data_patterns/        Unit of work, data mapper, active record, identity map
├── cloud_patterns/       Resilience and cloud-native patterns
├── resilience_patterns/  Timeout, hedge, fail-fast, fallback, load shedding
├── microservices_patterns/ API gateway, BFF, discovery, mesh, CQRS, sagas
├── distributed_patterns/ Leader election, gossip, CRDTs, 2PC, quorum, Raft
├── system_design/        Rate limiting, load balancing, caching, CAP, sharding
├── functional_patterns/  Monads, option/either, currying, pipelines
├── principles/           Engineering principles and heuristics
├── clean_architecture/   Hexagonal, onion, layered, dependency inversion
├── architecture_styles/  Monolith, modular monolith, microservices, serverless
├── security_patterns/    Zero trust, OAuth/OIDC, RBAC/ABAC, threat modeling
├── testing_patterns/     Test pyramid, doubles, property/contract/mutation
├── deployment_patterns/  Blue/green, canary, rolling, feature toggles
├── event_driven_patterns/ Event notification, state transfer, streams
├── observability_patterns/ Logging, metrics, tracing, health, correlation
├── ui_patterns/          MVC, MVP, MVVM, Flux, Redux, VIPER
├── templates/            ADR, RFC, design doc, runbook and C4 diagrams
└── api_design/           REST/GraphQL guidelines, versioning, pagination, errors
```

---

## Testing

```bash
# Run all architecture tests
make test-architectures

# Python patterns (includes linting, typechecking, and pytest)
cd architectures/python_patterns && bash lint.sh
```

---

## Additional Pattern Families

Beyond the original GoF, concurrency and distributed sets, the library now
includes enterprise integration, domain, data, cloud, resilience, microservices,
security, testing, deployment, event-driven, observability, UI and architecture
style families. Each family has an `index.md` mapping patterns to files.

Notable additions:

- **Integration:** pipes and filters, message translator, wire tap, publish/subscribe, competing consumers.
- **Data:** unit of work, data mapper, active record, identity map, lazy load, DAO.
- **Resilience:** timeout, hedge, fail-fast, fallback, load shedding, backpressure, throttling.
- **Microservices:** API gateway, BFF, service discovery/mesh, database per service, CQRS, event sourcing, saga orchestration, API composition.
- **Distributed:** leader election, gossip, vector clocks, CRDTs, two-phase commit, quorum, fencing tokens, Raft.
- **Functional:** monad, option/either, immutable value, currying, pipeline, memoization.
- **Security:** defense in depth, least privilege, zero trust, OAuth2/OIDC, JWT, RBAC/ABAC, threat modeling.
- **Testing:** test pyramid, test doubles, property-based, contract, golden master, mutation.
- **Deployment:** blue/green, canary, rolling update, feature toggles, shadow deployment, A/B testing.
- **Event-driven:** event notification, event-carried state transfer, event sourcing, event streams.
- **Observability:** structured logging, metrics, tracing, health checks, correlation IDs.
- **UI:** MVC, MVP, MVVM, Flux, Redux, VIPER.
- **Architecture styles:** monolith, modular monolith, microservices, serverless, event-driven, SOA, space-based, mesh.

Worked system-design case studies live in
`../interview_prep/system_design/designs/`.