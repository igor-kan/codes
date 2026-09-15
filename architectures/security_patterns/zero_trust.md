# Zero Trust

"Never trust, always verify": no implicit trust based on network location.

## Pillars

- **Identity:** strong, phishing-resistant authentication (MFA/WebAuthn).
- **Device:** posture checks before access.
- **Network:** micro-segmentation and mutual TLS.
- **Application:** per-request authorization.
- **Data:** classification, encryption, and DLP.

## Practices

- Authenticate and authorize every request.
- Assume breach; limit lateral movement.
- Centralize policy with continuous verification.
- Log everything and detect anomalies.

Related: Defense in Depth, Least Privilege, Service Mesh (mTLS).
