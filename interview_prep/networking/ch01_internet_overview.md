# Networking: Internet Overview (Ch. 1)

## The network edge and core

- **Edge:** hosts, clients, servers; access networks (DSL, cable, fiber, 5G, WiFi).
- **Core:** packet switches (routers, switches) interconnected by links.
- **Circuit switching** reserves resources; **packet switching** multiplexes on demand.

## Layered architecture

| Layer | Data unit | Protocols |
|:---|:---|:---|
| Application | message | HTTP, SMTP, DNS, QUIC |
| Transport | segment | TCP, UDP |
| Network | datagram | IP, ICMP, routing |
| Link | frame | Ethernet, WiFi, ARP |
| Physical | bit | copper, fiber, radio |

## Performance metrics

- **Bandwidth** (bits/sec) and **throughput** (actual rate).
- **Delay:** processing + queueing + transmission + propagation.
- **Bandwidth-delay product:** bits "in flight" on a link.
- **Packet loss** from buffer overflow; **jitter** from variable queueing.

See `packet_delay.py` for a delay model.
