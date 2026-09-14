# TAGE Branch Prediction

**TAge** (TAgged GEometric history length) is a leading branch predictor that
uses several prediction tables indexed by different history lengths.

## Idea

- Maintain a global history register.
- Use tables with history lengths forming a geometric series (e.g. 0, 2, 4, 8,
  16, 32, 64, 128 bits).
- Each entry is **tagged** to reduce aliasing; the longest matching entry wins.
- A **usefulness** counter decides whether to allocate new entries, so longer
  histories are learned only when they help.

## Why it works

- Short histories capture simple patterns and loops.
- Long histories capture complex correlations (e.g. nested conditions).
- Tags plus usefulness counters keep the tables accurate without unbounded size.

## Practical notes

- Combined with a BTB, RAS, and a loop predictor.
- Variants: TAGE-SC-L (statistical corrector + loop predictor).
- Powers much of the performance measured in SPEC CPU.
