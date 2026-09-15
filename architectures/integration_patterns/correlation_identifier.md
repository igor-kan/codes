# Correlation Identifier

Attach an identifier to a request so that replies can be matched to it when
responses arrive asynchronously.

## Uses

- Request/reply over a queue.
- Aggregating multi-step workflows.
- Distributed tracing (trace/span IDs).

## Guidance

- Generate a unique, opaque ID at the origin.
- Propagate it through every hop and log it consistently.
- Keep IDs in the envelope, not the domain payload.
- Bound their lifetime and size; never use them as secrets.

Related: Envelope Wrapper, Message Store, Observability.
