# The Internet's Edge and Core

## Edge

- **Hosts:** clients and servers running applications.
- **Access networks:** DSL, cable (HFC), FTTH, 5G, enterprise and WiFi.
- **Physical media:** twisted pair, coax, fiber, radio.

## Core

- **Packet switching:** store-and-forward, statistical multiplexing, queues.
- **Circuit switching:** reserved end-to-end capacity (FDM/TDM).
- **Network of networks:** ISPs tiered (tier-1, regional, access), peering and
  transit, Internet Exchange Points (IXPs).
- **Content providers** build private backbones and peer directly with ISPs.

## Delay components

`nodal delay = processing + queueing + transmission + propagation`

- Transmission = packet length / link rate.
- Propagation = distance / propagation speed.
- Queueing depends on traffic intensity (Laplace/Kleinrock).

## Loss and throughput

Buffers overflow, causing loss and retransmission. Bottleneck link determines
end-to-end throughput.
