# `std::unordered_map` Internals

A hash table with **separate chaining**: an array of buckets, each a linked list.

## Operations

- `O(1)` average, `O(n)` worst case (all keys collide).
- `max_load_factor()` (default 1.0) triggers rehashing when exceeded.
- Rehash invalidates all iterators; `reserve` avoids repeated rehashing.

## Hash strategy

- Uses `std::hash<K>`; combine with a good `operator==`.
- For adversarial input, use a randomized hash (SipHash) to prevent
  hash-flooding DoS.

## Why `O(1)` reads are not cache-friendly

Each lookup chases a pointer into a list node, causing a cache miss. Open
addressing variants (`flat_hash_map`, `robin_hood`) probe contiguous memory and
are markedly faster.

## Bucket API

`bucket_count`, `bucket(key)`, `load_factor`, `rehash`, `reserve`.
