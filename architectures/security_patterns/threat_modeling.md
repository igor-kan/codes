# Threat Modeling

Systematically identify threats and mitigations during design.

## STRIDE

| Threat | Violates |
|:---|:---|
| Spoofing | authentication |
| Tampering | integrity |
| Repudiation | non-repudiation |
| Information disclosure | confidentiality |
| Denial of service | availability |
| Elevation of privilege | authorization |

## Process

1. Diagram the system and trust boundaries (data-flow diagram).
2. Enumerate threats per component/boundary.
3. Rate risk (likelihood × impact) and prioritize.
4. Define mitigations and tests; track to closure.
5. Revisit when the design changes.

Related: Defense in Depth, OWASP ASVS, Attack Trees.
