# Pagination

## Offset / limit

```
GET /orders?page=3&perPage=50
```

- Simple, supports random access and total counts.
- Degrades on large offsets (`OFFSET 100000`) and can skip/duplicate rows when
  the underlying data changes.

## Cursor / keyset

```
GET /orders?limit=50&after=eyJpZCI6MTAwfQ
```

- Stable under inserts/deletes; efficient with an indexed `(sort_key, id)`.
- No random access or total count; opaque cursor should be signed.
- Prefer for feeds, timelines, and high-volume collections.

## Response envelope

```json
{
  "data": ["..."],
  "pageInfo": {
    "hasNextPage": true,
    "endCursor": "eyJpZCI6MTUwfQ"
  },
  "totalCount": 10432
}
```

## Guidance

- Cap `perPage` (e.g. 100) to protect the backend.
- Document the sort order; make it deterministic with a tiebreaker key.
- For GraphQL, follow the Relay Connections specification.

Related: REST Guidelines, Sharding.
