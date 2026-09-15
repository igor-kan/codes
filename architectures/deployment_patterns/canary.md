# Canary Deployment

Release to a small subset of traffic, compare metrics to the baseline, then
gradually increase.

## Steps

1. Deploy the new version to a small percentage.
2. Watch error rate, latency, saturation, and business KPIs.
3. Increase traffic if healthy; roll back automatically on regression.

## Requirements

- Traffic splitting (service mesh/ingress) and per-version metrics.
- Automated analysis with clear abort criteria.

Related: Blue/Green, Feature Toggle, Observability.
