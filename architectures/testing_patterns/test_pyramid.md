# The Test Pyramid

Fast, cheap tests at the base; fewer, slower end-to-end tests at the top.

```
        /\  E2E (few, slow, brittle)
       /  \
      /____\ Integration (some)
     /      \
    /________\ Unit (many, fast, isolated)
```

## Guidance

- Push logic down to unit tests; reserve E2E for critical journeys.
- Keep tests deterministic and independent.
- Treat flaky tests as bugs; fix or delete them.
- Measure coverage as a signal, not a goal.

Related: Test Doubles, Contract Testing.
