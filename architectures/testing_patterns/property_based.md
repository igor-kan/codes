# Property-Based Testing

Instead of examples, assert **properties** that hold for all inputs; the
framework generates cases and shrinks failures.

## Example properties

- `reverse(reverse(xs)) == xs`
- sorting is idempotent and preserves multiset
- encode/decode round-trips
- `len(concat(a, b)) == len(a) + len(b)`

## Benefits

- Finds edge cases you would not write (empty, unicode, overflow).
- Shrinking produces minimal counterexamples.

Tools: Hypothesis (Python), QuickCheck (Haskell), fast-check (TS), proptest
(Rust), jqwik (Java).

Related: Mutation Testing, Fuzzing.
