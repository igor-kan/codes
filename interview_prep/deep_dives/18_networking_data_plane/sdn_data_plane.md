# SDN Data Plane

Software-Defined Networking separates the **control plane** (a logically
centralized controller) from the **data plane** (simple forwarding devices).

## Match + action

OpenFlow flow tables match on header fields and apply actions:

| Match | Action |
|:---|:---|
| `in_port`, `eth_src`, `eth_dst` | forward, flood, drop |
| `ipv4_dst = 10.0.0.0/8` | set next hop, decrement TTL |
| `tcp_dst = 80` | push/pop VLAN, encapsulate |

## Pipeline

Multiple tables with goto, meters and groups implement policies (ACLs, load
balancing, tunnelling) without changing hardware logic.

## Programmable data planes

- **P4:** describes parsers, match-action tables and deparsers in a portable
  language, compiled to switches/DPUs/smart NICs.
- **eBPF/XDP:** program the Linux data path at the driver level.

## Benefits and challenges

Central visibility and agile policy vs. controller scalability, consistency, and
table-size limits.
