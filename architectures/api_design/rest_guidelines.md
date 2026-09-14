# REST API Guidelines

## Resources and URLs

- Use **nouns**, plural, lower-kebab-case: `/orders`, `/users/{id}/addresses`.
- Let the HTTP method be the verb; avoid `/getUser`.
- Nest only one level; use query filters beyond that.
- Identifiers are opaque (`uuid`) and never encode guessable sequences.

## Methods and semantics

| Method | Idempotent | Safe | Purpose |
|:---|:---|:---|:---|
| GET | yes | yes | retrieve |
| POST | no | no | create / action |
| PUT | yes | no | full replace |
| PATCH | no | no | partial update |
| DELETE | yes | no | remove |

## Status codes

- `200/201/204` success; `201` sets `Location`.
- `400` validation, `401` unauthenticated, `403` forbidden, `404` missing.
- `409` conflict, `412` precondition, `422` semantic error, `429` throttled.
- `5xx` never leaks internals.

## Conventions

- Always return JSON; lowercase field names.
- Support idempotency keys for unsafe retried requests.
- Version via media type or URL prefix; never break a live contract.
- Provide `ETag`/`If-Match` for optimistic concurrency.

Related: Versioning, Pagination, Error Handling.
