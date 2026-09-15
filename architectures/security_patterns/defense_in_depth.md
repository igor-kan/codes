# Defense in Depth

Layer independent controls so no single failure exposes the system.

## Layers

1. Network: segmentation, firewalls, WAF, DDoS protection.
2. Host: hardening, patching, EDR, least-privilege service accounts.
3. Application: input validation, output encoding, authN/authZ.
4. Data: encryption at rest/in transit, tokenization, backups.
5. People/process: reviews, training, incident response.

## Principles

- Assume each layer can fail.
- Prefer simple, auditable controls.
- Monitor and alert at every layer; log tamper-evidently.

Related: Zero Trust, Least Privilege, Threat Modeling.
