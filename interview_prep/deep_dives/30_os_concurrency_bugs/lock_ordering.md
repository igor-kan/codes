# Lock Ordering

Impose a total order on locks and always acquire in that order; this eliminates
circular wait, the fourth Coffman condition.

## Practice

- Assign a numeric rank to each lock; assert rank strictly increases.
- Use a **hierarchical mutex** that enforces this at runtime (throws on
  violation).
- Prefer a single lock or `std::scoped_lock` over manual multi-lock code.
- Document the order next to the lock declarations.

## Example (C++)

```cpp
std::scoped_lock lock(accounts[a], accounts[b]); // deadlock-free multi-lock
```

`std::lock`/`scoped_lock` implement a deadlock-avoidance algorithm internally.

## Dynamic ordering

When objects have no static rank, order by a stable key (address, id) before
locking. Never lock in caller-supplied order.
