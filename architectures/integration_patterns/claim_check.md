# Claim Check

Pass large payloads by reference: store the data, send only a **claim check**
(token/key) in the message.

## Flow

1. Producer stores the payload in a data store and puts the key in the message.
2. Consumers fetch the payload by key when needed.
3. A janitor purges expired payloads.

## Benefits

- Keeps messages small and brokers fast.
- Works around message size limits.

## Costs

- Extra store, extra round trip, lifecycle/GC management.
- Security: the key must be authorized and tamper-proof.

Related: Message Store, Envelope Wrapper.
