# Hexagonal Architecture (Ports and Adapters)

Place the application core (domain + use cases) at the center and connect it to
the outside world only through **ports** (interfaces) and **adapters**
(implementations).

```
        [ HTTP adapter ]                 [ CLI adapter ]
                 \                        /
              ports/  (driving)   (driven)  \ ports
                        \    [ USE CASES ]    /
                         \   [  DOMAIN   ]   /
              ports/  (driven)           (driven) / ports
                 /                        \
        [ Postgres adapter ]        [ Message-bus adapter ]
```

- **Driving (primary) adapters** invoke the core: HTTP controllers, CLI, tests.
- **Driven (secondary) adapters** are invoked by the core: repositories, gateways.
- Ports are defined in terms of the domain's types, not the technology.

**Benefits:** the core is framework- and database-independent and fast to test;
technology choices become reversible.

Related: Clean Architecture, Onion Architecture, Dependency Inversion.
