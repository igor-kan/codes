# DNS: The Internet's Directory

## Hierarchy

Root servers → top-level domains (`.com`, `.org`) → authoritative servers for
zones. Resolvers cache results according to TTL.

## Resolution

1. Stub resolver asks a **recursive** resolver.
2. If uncached, the resolver walks root → TLD → authoritative (**iterative**).
3. Answer is cached; TTL controls freshness.

## Record types

| Type | Meaning |
|:---|:---|
| A / AAAA | IPv4 / IPv6 address |
| CNAME | canonical name alias |
| MX | mail exchanger |
| NS | authoritative name server |
| TXT | arbitrary text (SPF, DKIM, verification) |
| SOA | zone authority metadata |
| SRV | service location |

## Reliability and security

- UDP by default; TCP for large responses and zone transfers.
- DNSSEC signs records to prevent spoofing.
- DNS over TLS/HTTPS encrypts queries.
- Anycast spreads root and public resolvers globally.
