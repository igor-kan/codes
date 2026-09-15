# Hand-Over-Hand Locking

Each node of a linked structure has its own lock. A traversal acquires the next
node's lock **before** releasing the current one, so the chain is never
unprotected.

```
lock(head)
cur = head
while cur.next != target:
    lock(cur.next)
    unlock(cur)
    cur = cur.next
```

## Pros and cons

- **Pro:** concurrency across disjoint regions and no gap during traversal.
- **Con:** each hop is a lock acquire/release, so total cost is high; in practice
  usually slower than a single lock for short lists.
- **Con:** deadlock risk if traversal order is inconsistent; always lock in a
  fixed direction.

## Variants

- **Lazy locking:** a node is marked removed before being unlinked; contains
  validates after locking.
- **Optimistic traversal:** read without locks, then validate under locks.
- **RCU:** read-copy-update lets readers proceed lock-free while writers publish
  new versions.

Use fine-grained locking only when measurements show contention.
