# Feature Toggles

Decouple **deploy** from **release**: merge code behind a flag, enable it at
runtime for chosen users.

## Categories

- **Release toggles:** short-lived, gate new functionality.
- **Ops toggles:** kill switches and circuit breakers.
- **Experiment toggles:** A/B tests.
- **Permission toggles:** entitlements.

## Hygiene

- Name and document every flag; assign an owner and expiry.
- Remove stale flags promptly to avoid combinatorial complexity.
- Evaluate flags server-side and avoid nesting.

Related: A/B Testing, Progressive Delivery.
