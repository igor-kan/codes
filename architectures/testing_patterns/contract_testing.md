# Contract Testing

Verify that a consumer and provider agree on an interface without running both
together.

## Flow

1. Consumer defines expectations ("pact") from recorded interactions.
2. Provider replays them in CI and publishes verification results.
3. A broker gates deployment on compatible versions.

## Benefits

- Decouples teams; catches breaking changes pre-deploy.
- Fast, stable alternative to full integration environments.

Tools: Pact, Spring Cloud Contract.

Related: Microservices, API Versioning.
