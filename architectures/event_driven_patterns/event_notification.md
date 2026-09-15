# Event Notification

Publish a minimal event ("order-created: id=7") and let consumers query for
details.

## Pros

- Small messages; low coupling to details.
- Easy to add consumers.

## Cons

- Consumers call back (chatty, load spikes).
- Correlation and ordering are harder.

Related: Event-Carried State Transfer, Claim Check.
