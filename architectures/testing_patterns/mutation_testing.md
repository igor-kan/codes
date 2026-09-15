# Mutation Testing

Assess test-suite quality by injecting small faults (mutants) and checking that
tests fail.

## Mutation operators

- Change `<` to `<=`, `+` to `-`, swap constants.
- Remove statements, negate conditions.

## Metrics

- **Mutation score** = killed / total mutants.
- Surviving mutants reveal weak assertions or dead code.

## Practice

- Run on changed code in CI (mutation testing is expensive).
- Treat surviving mutants as review prompts, not absolute failures.

Tools: Stryker, PIT, mutmut, cargo-mutants.

Related: Property-Based Testing, Coverage.
