# Layering and Encapsulation

Each layer offers a service to the layer above and uses the service below,
communicating logically with its peer.

| Layer | PDU | Addressing | Example |
|:---|:---|:---|:---|
| Application | message | names/URLs | HTTP, DNS, SMTP |
| Transport | segment/datagram | ports | TCP, UDP, QUIC |
| Network | packet | IP addresses | IPv4, IPv6, ICMP |
| Link | frame | MAC addresses | Ethernet, WiFi, ARP |
| Physical | bit | — | fiber, copper, radio |

## Encapsulation

```
[ Ethernet [ IP [ TCP [ HTTP payload ] ] ] ]
```

Each layer prepends its header; decapsulation reverses the process.

## Benefits and costs

- **Modularity:** replace a layer without touching others.
- **Cost:** duplicated functionality, header overhead, cross-layer tuning needed
  for performance (e.g. TCP over WiFi).

## Internet hourglass

IP is the narrow waist: many application protocols above, many link technologies
below. It is why the Internet is extensible.
