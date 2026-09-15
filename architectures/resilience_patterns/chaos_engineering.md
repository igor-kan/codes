# Chaos Engineering

Deliberately inject failures into production-like environments to find
weaknesses before they cause outages.

## Method

1. Define a **steady state** (measurable normal behaviour).
2. Form a hypothesis ("the system tolerates a zone failure").
3. Inject a controlled fault (kill a node, add latency, drop packets).
4. Measure deviation from steady state.
5. Fix weaknesses; automate the experiment.

## Common experiments

- Instance/zone termination.
- Network latency, packet loss, DNS failure.
- Dependency failure and slow responses.
- Clock skew and disk-full conditions.

## Safety

- Blast-radius controls, kill switch, and off-hours windows.
- Start in staging; graduate to production with guardrails.
- Never run without observability and an on-call owner.

Related: Resilience Patterns, Observability, GameDays.
