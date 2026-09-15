# `std::map` Internals

`std::map` is a balanced binary search tree, almost always a **red-black tree**.

## Guarantees

- Ordered by key (comparator), unique keys.
- `O(log n)` search, insert, erase.
- Iterators stable across insertions; erase invalidates only erased nodes.

## Node layout

Each node stores the key, value, three pointers (left, right, parent) and a
colour bit. This overhead is why `map` has poor cache locality.

## Red-black invariants

1. Every node is red or black.
2. Root and leaves (nil) are black.
3. Red nodes have black children.
4. Equal black height on all root-to-leaf paths.

Rotations and recolouring restore these after insert/erase.

## Alternatives

- `unordered_map`: hash table, average `O(1)`, no ordering.
- `flat_map` / sorted vector: cache-friendly, good for read-heavy workloads.
- B-trees (`absl::btree_map`) for large nodes and fewer cache misses.
