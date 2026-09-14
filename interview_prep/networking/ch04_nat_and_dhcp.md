# NAT and DHCP

## NAT (Network Address Translation)

Maps private addresses (RFC 1918: 10/8, 172.16/12, 192.168/16) to a public
address, rewriting source ports to disambiguate flows.

- **SNAT** rewrites outgoing source; **DNAT** rewrites inbound destination.
- Conserves IPv4 space and hides internal topology.
- Breaks end-to-end connectivity; complicates peer-to-peer and inbound servers.
- Requires hole punching, STUN/TURN, or port forwarding.

## DHCP (Dynamic Host Configuration Protocol)

Automatically assigns addresses and network parameters.

1. **Discover** (client broadcast)
2. **Offer** (server proposes an address)
3. **Request** (client accepts)
4. **Acknowledge** (server confirms lease)

Leases expire and are renewed; options include gateway, DNS servers, and MTU.

## Related

- ARP maps IP → MAC within a LAN.
- ICMP supports diagnostics (`ping`, `traceroute`).
