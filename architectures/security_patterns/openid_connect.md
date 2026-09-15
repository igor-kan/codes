# OpenID Connect (OIDC)

An identity layer on top of OAuth 2.0 that issues an **ID token** (a JWT)
asserting who the user is.

## Additions to OAuth

- `openid` scope and an `id_token`.
- UserInfo endpoint and standard claims (`sub`, `email`, `name`).
- Discovery document and JWKS for key rotation.

## Validation

- Verify the signature against JWKS.
- Check `iss`, `aud`, `exp`, and nonce.
- Never use an ID token as an API access token.

Related: OAuth 2.0, JWT, SSO.
