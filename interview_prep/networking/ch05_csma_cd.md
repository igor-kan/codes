# CSMA/CD and CSMA/CA

## CSMA/CD (wired Ethernet)

1. **Carrier sense:** listen before transmitting.
2. **Collision detection:** detect overlapping transmissions.
3. **Jam signal** and **binary exponential backoff:** wait a random number of
   slot times, doubling the contention window on repeated collisions.
4. Give up after 16 attempts and report an error.

## CSMA/CA (802.11 wireless)

Wireless cannot easily detect collisions, so it *avoids* them:

1. Sense the medium; if idle, wait a DIFS then transmit.
2. Receiver ACKs after SIFS; missing ACK ⇒ retransmit with backoff.
3. Optional **RTS/CTS** handshake reserves the medium and mitigates the
   **hidden-terminal** problem.

## Throughput

Efficiency depends on propagation delay and frame size; CSMA/CD efficiency
approaches `1 / (1 + 5 * propagation / transmission)`.
