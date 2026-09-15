# Shadow Deployment

Mirror production traffic to a new version whose responses are discarded, to
validate behaviour and performance with zero user risk.

## Uses

- Compare outputs of a rewrite against the incumbent.
- Load-test the new version with real traffic patterns.

## Cautions

- Side effects must be suppressed (writes, emails, payments).
- Double resource cost and potential data-leak risk.

Related: Canary, A/B Testing, Strangler Fig.
