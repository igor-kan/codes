# Branch Prediction

Modern CPUs speculate past branches; correct prediction keeps the pipeline full.
A misprediction flushes the pipeline and costs 10-20+ cycles.

## Predictors

| Predictor | History | Notes |
|:---|:---|:---|
| Always not-taken | none | baseline |
| BTFN | direction bias | backward-taken, forward-not |
| 1-bit | last outcome | flips on one anomaly |
| 2-bit saturating | last two | hysteresis reduces flips |
| Correlating (gshare) | global history XOR PC | captures patterns |
| TAGE | variable-length history | state of the art |

## Components

- **BTB** (branch target buffer): caches target addresses.
- **RAS** (return address stack): predicts function returns.
- **Loop predictor:** special-cases counted loops.

## Costs and defenses

- Mispredict penalty scales with pipeline depth and issue width.
- Speculative execution opens side channels (Spectre); mitigations include
  barriers, retpolines, and disabling speculation on sensitive paths.
