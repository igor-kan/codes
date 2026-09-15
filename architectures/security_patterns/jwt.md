# JSON Web Tokens (JWT)

Compact, signed (JWS) or encrypted (JWE) claims used for authentication and
authorization.

## Structure

`base64url(header).base64url(payload).base64url(signature)`

## Best practices

- Prefer asymmetric signatures (RS256/ES256) and verify against JWKS.
- Validate `iss`, `aud`, `exp`, `nbf`, and algorithm (reject `none`/confusion).
- Keep tokens short-lived; use refresh tokens for longevity.
- Do not store secrets or PII in the payload (it is only encoded).
- Support revocation for high-value sessions (denylist or short TTL).

Related: OAuth 2.0, OIDC, Session Management.
