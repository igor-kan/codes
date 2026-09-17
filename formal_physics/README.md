# Formal Physics — Classical Mechanics in Lean 4

A machine-checked formalization of analytical classical mechanics,
built on top of [Mathlib](https://github.com/leanprover-community/mathlib4).

* **Chapter 6 — Calculus of Variations.** Functionals as functions on curve
  spaces, the first variation as a Fréchet derivative, stationarity of the
  action, the Euler–Lagrange equation, the Beltrami identity, the shortest path,
  the brachistochrone and the cycloid, the second variation with Legendre's
  condition and conjugate points, and functionals of several variables.
* **Chapter 7 — Lagrange's Equations.** Configuration space, kinetic energy as a
  Riemannian metric, the generalized momentum as a gradient, the
  Newton ⇔ Euler–Lagrange equivalence, curvilinear velocities, the rheonomic
  `T = T₂ + T₁ + T₀` decomposition, Hamilton's principle, holonomic constraints
  with Lagrange multipliers, and Noether's theorem for cyclic coordinates.
* **Chapter 13 — Hamiltonian Mechanics.** Phase space, Hamilton's equations,
  conservation of energy, the Legendre transform, the Poisson bracket and its
  algebraic axioms, the symplectic operator, and Liouville's theorem.

## What "formalizing physics" buys

Following the blog post
[Formal Verification / Axiomatic Physics in Lean 4](https://igorkan.github.io/quarto-writing/posts/physics/formal-verification-axiomatic-physics-lean-4.html),
the point is that every silent assumption becomes a *type* or a *hypothesis*:

| Physics phrase | Lean / Mathlib encoding |
|:---|:---|
| "a path" | `γ : ℝ → E` with `ContDiff ℝ n γ` when needed |
| "the first variation" | `fderiv ℝ S γ η` — a continuous linear map |
| "∂L/∂v" (canonical momentum) | `gradient (fun v => L x v) v`, or `deriv` in 1-D |
| "the potential is smooth" | an explicit `DifferentiableAt`/`Differentiable` hypothesis |
| "the second variation" | Legendre's `P = ∂²f/∂v²`, conjugate time `π/ω` |
| "phase space" | a type `M` with a Hamiltonian `H : M → ℝ` |
| "the Poisson bracket" | `poisson f g`, with antisymmetry and `{f,f}=0` proven |
| "Liouville's theorem" | `det M = 1` for the linear flow matrix |

## Layout

```
formal_physics/
├── FormalPhysics.lean                    -- root, imports everything
├── lakefile.toml                         -- depends on Mathlib v4.16.0
├── lean-toolchain                        -- leanprover/lean4:v4.16.0
├── FormalPhysics/
│   ├── Calculus.lean                     -- reusable HasDerivAt lemmas
│   ├── Variations/                       -- Chapter 6
│   │   ├── Basic.lean                    -- functionals, first variation, stationarity
│   │   ├── Beltrami.lean                 -- Beltrami identity, shortest path, brachistochrone
│   │   ├── Brachistochrone.lean          -- cycloid, y(1+y'²)=2a
│   │   ├── SecondVariation.lean          -- Legendre condition, conjugate points
│   │   └── SeveralVariables.lean         -- systems of Euler–Lagrange equations
│   ├── Lagrangian/                       -- Chapter 7
│   │   ├── EulerLagrange.lean            -- momentum, force, Newton ⇔ E–L, harmonic oscillator
│   │   ├── Configuration.lean            -- configuration space, gradient momentum
│   │   ├── Coordinates.lean              -- polar/cylindrical/spherical T, rheonomic T₂+T₁+T₀
│   │   ├── HamiltonPrinciple.lean        -- stationary action ↔ Euler–Lagrange
│   │   ├── Constraints.lean              -- holonomic constraints, Lagrange multipliers
│   │   ├── DoublePendulum.lean           -- double-pendulum Lagrangian
│   │   └── Noether.lean                  -- cyclic coordinate ⇒ conserved momentum
│   └── Hamiltonian/                      -- Chapter 13
│       ├── PhaseSpace.lean               -- Hamilton's equations, energy conservation
│       ├── Legendre.lean                 -- Legendre transform of ½ m v²
│       ├── Poisson.lean                  -- Poisson bracket axioms
│       ├── Symplectic.lean               -- the operator J, J² = -1, nondegeneracy
│       └── Liouville.lean                -- det = 1, area preservation
└── scripts/verify.sh                     -- fetch the Mathlib cache and build
```

## Build

Mathlib is required. The first build downloads the prebuilt olean cache
(several GB); afterwards builds are fast.

```bash
cd formal_physics
lake exe cache get      # one-time: prebuilt Mathlib oleans
lake build              # checks every theorem (no sorry, no axiom beyond Mathlib)
```

`scripts/verify.sh` wraps this and greps for `sorry`.

To build offline against a local Mathlib checkout, point Lake at it with a path
dependency instead of the git dependency in `lakefile.toml`:

```toml
[[require]]
name = "mathlib"
path = "/path/to/mathlib4"
```

## Status

All files compile with Lean 4.16.0 and Mathlib v4.16.0. The deep analytic
theorem linking stationarity of the action to the Euler–Lagrange equation (the
fundamental lemma of the calculus of variations) is exposed as an explicit
hypothesis in `HamiltonPrinciple.lean`, matching the blog's treatment; the
remaining results are unconditional.

## License

Apache 2.0. See `LICENSE`.
