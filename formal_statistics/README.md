# Formal Statistics — Kutner's *Applied Linear Statistical Models* in Lean 4

A machine-checked formalization of **Chapter 1** (linear regression with one
predictor variable) and **Chapter 2** (inferences in regression and correlation
analysis) of Kutner, Nachtsheim & Neter, *Applied Linear Statistical Models*,
built on [Mathlib](https://github.com/leanprover-community/mathlib4).

## What is formalized

| Kutner | Result | Lean name |
|:---|:---|:---|
| §1.6 | least-squares estimates `b₁ = Sxy/Sxx`, `b₀ = ȳ - b₁x̄` | `b1`, `b0` |
| §1.6 | the two normal equations `Σeᵢ = 0`, `Σxᵢeᵢ = 0` | `residual_sum`, `residual_orthogonal` |
| §1.6 | **master decomposition** `Q = SSE + n(β₀+β₁x̄-ȳ)² + Sxx(β₁-b₁)²` | `Q_decomposition` |
| §1.6 | `(b₀,b₁)` is the unique minimizer of `Q` (non-constant predictor) | `isMinOn_Q`, `Q_eq_SSE_iff` |
| §1.7 | `MSE = SSE/(n-2)`, error variance estimate | `MSE` |
| §2.7 | **sum-of-squares decomposition** `SSTO = SSR + SSE` | `SSTO_eq_SSR_add_SSE` |
| §2.7 | ANOVA `F = t²` | `FStat_eq_tStat_sq` |
| §2.9 | coefficient of determination `R² ∈ [0,1]`, `R² = 1 - SSE/SSTO` | `R2_eq_one_sub`, `R2_nonneg`, `R2_le_one` |
| §2.9/11 | correlation `r = Sxy/√(Sxx·Syy)`, **Cauchy–Schwarz** `Sxy² ≤ Sxx·Syy`, `|r| ≤ 1`, `r² = R²` | `Sxy_sq_le`, `abs_corr_le_one`, `corr_sq_eq_R2` |
| §1.3/2.1 | additive error model `b₁ - β₁ = Σ cᵢ εᵢ`, `cᵢ=(xᵢ-x̄)/Sxx` | `b1_sub_eq_cvec`, `b0_sub_eq` |

Everything is proved by the Lean kernel; there are **no `sorry`s** and no axioms
beyond Mathlib.

## Mathlib libraries used

- `Finset` sums and `Finset.sum_mul_sq_le_sq_mul_sq` (Cauchy–Schwarz) for the
  sampling theory and `|r| ≤ 1`.
- `field_simp`, `ring`, `linarith`/`nlinarith` for the algebraic identities.
- `Real.sqrt` lemmas (`Real.sq_sqrt`, `Real.sqrt_sq_eq_abs`, `Real.sqrt_le_one`)
  for the standard errors and correlation.
- The project is structured to be extended with `ProbabilityTheory`
  (`Mathlib.Probability.Distributions.Gaussian`, `Mathlib.Probability.Variance`,
  `Mathlib.Probability.Moments`) for the distributional statements of §2.1–2.6.

## Layout

```
formal_statistics/
├── FormalStatistics.lean              -- root, imports every module
├── lakefile.toml                      -- Mathlib v4.16.0 dependency
├── lean-toolchain                     -- leanprover/lean4:v4.16.0
├── FormalStatistics/
│   ├── Data.lean                      -- mean, Sxx, Sxy, Syy
│   ├── NormalEquations.lean           -- b0, b1, residual, normal equations
│   ├── LeastSquares.lean              -- Q, master decomposition, minimizer, uniqueness
│   ├── GoodnessOfFit.lean             -- SSTO = SSR + SSE, R²
│   ├── Correlation.lean               -- r, Cauchy–Schwarz, r² = R²
│   ├── ErrorModel.lean                -- additive model, b₁ - β₁ = Σ cᵢ εᵢ
│   └── Inference.lean                 -- MSE, s{b₁}, t, F = t², prediction SEs
└── scripts/verify.sh                  -- fetch Mathlib cache and build
```

## Build

```bash
cd formal_statistics
lake exe cache get     # one-time: prebuilt Mathlib oleans
lake build
```

`scripts/verify.sh` wraps this and checks for `sorry`.

## Attribution

Text: Kutner, Nachtsheim & Neter, *Applied Linear Statistical Models*.
Library: [Mathlib4](https://github.com/leanprover-community/mathlib4) (Apache-2.0),
Lean 4 (Apache-2.0). Licensed under Apache-2.0; see `LICENSE`.
