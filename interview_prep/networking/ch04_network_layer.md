# Network Layer (Ch. 4)

## Data plane

- **IPv4/IPv6** addressing and forwarding.
- Longest-prefix match on the forwarding table.
- Fragmentation, TTL/hop limit, and ICMP errors.
- NAT rewrites addresses/ports at the edge.

## Control plane

- Routing protocols: RIP (distance vector), OSPF (link state), BGP (path vector).
- Autonomous systems and policy routing.
- Middleboxes: firewalls, load balancers, NAT, DPI.

## IPv4 header fields

| Field | Purpose |
|:---|:---|
| version/IHL | protocol version and header length |
| total length | datagram size in bytes |
| TTL | decremented per router; drops at 0 |
| protocol | upper layer (6=TCP, 17=UDP, 1=ICMP) |
| src/dst | 32-bit addresses |
| checksum | header-only integrity |

## Addressing

- Classless inter-domain routing (CIDR) and prefix aggregation.
- IPv6: 128-bit addresses, no header checksum, simplified header.
