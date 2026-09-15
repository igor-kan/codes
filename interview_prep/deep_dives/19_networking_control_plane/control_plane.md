# Network Layer: Control Plane

Decides how packets are routed; populates forwarding tables in the data plane.

## Routing algorithm classes

- **Link-state (OSPF, IS-IS):** every router floods link state and runs
  Dijkstra on the full topology.
- **Distance-vector (RIP):** routers exchange vectors of costs; Bellman-Ford
  updates propagate ("routing by rumor").
- **Path-vector (BGP):** ASes advertise reachability with the full AS path,
  enabling policy routing.

## Autonomous systems

- **Intra-AS (IGP):** OSPF, IS-IS, RIP/EIGRP.
- **Inter-AS (EGP):** BGP-4. Business relationships (customer/provider, peer)
  shape policy.

## ICMP

Error and control messages: destination unreachable, time exceeded, echo
request/reply; used by `ping` and `traceroute`.

## SDN control plane

A logically central controller computes routes and installs flows; interfaces
such as OpenFlow, P4Runtime, and NETCONF/YANG.

## Convergence and loops

Count-to-infinity, split horizon, poison reverse; hold-down timers; loop
prevention in BGP (AS-path) and MPLS.
