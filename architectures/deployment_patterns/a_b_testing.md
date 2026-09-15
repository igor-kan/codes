# A/B Testing

Split users between variants and measure the effect on a defined metric.

## Steps

1. State a hypothesis and primary metric (plus guardrails).
2. Randomize assignment consistently per user.
3. Run long enough for statistical power; avoid peeking.
4. Analyze with confidence intervals; watch for novelty effects.

## Pitfalls

- Multiple comparisons and p-hacking.
- Sample-ratio mismatch and assignment bias.
- Optimizing a proxy metric that harms the goal.

Related: Feature Toggle, Experimentation Platform.
