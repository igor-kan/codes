# OAuth 2.0

An authorization framework for delegated access to resources without sharing
passwords.

## Roles

Resource owner, client, authorization server, resource server.

## Flows

| Flow | Use |
|:---|:---|
| Authorization Code + PKCE | web/mobile/native (preferred) |
| Client Credentials | machine-to-machine |
| Device Code | TVs/CLI |
| Refresh Token | long-lived sessions |
| (Implicit, Password) | deprecated |

## Security

- Always use PKCE; never expose client secrets in public clients.
- Validate `state` (CSRF) and `redirect_uri` (exact match).
- Use short-lived access tokens and scoped permissions.

Related: OpenID Connect, JWT, Zero Trust.
