# Monads

A monad wraps a value in a context and provides `bind` (flatMap) to sequence
computations within that context.

## Intuition

```
pure(x) -> M x
bind(M x, f: x -> M y) -> M y
```

## Common monads

| Monad | Context | Example use |
|:---|:---|:---|
| Option/Maybe | possible absence | lookups |
| Either/Result | errors | fallible steps |
| Future/Promise | async | I/O sequencing |
| List | non-determinism | branching |
| Reader | environment | dependency injection |
| State | mutable state | interpreters |

## Laws

Left identity, right identity, associativity — they make refactoring safe.

Related: Option/Either, Futures, Pipeline.
