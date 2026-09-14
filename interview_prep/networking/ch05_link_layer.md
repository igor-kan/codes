# Link Layer (Ch. 5)

## Services

- **Framing** and link access (MAC protocols).
- **Reliable delivery** on error-prone links (optional).
- **Error detection/correction** and flow control.

## Error detection

- **Parity** (single-bit), **checksum** (transport), **CRC** (link).
- CRC treats bits as a polynomial and divides by a generator; the remainder is
  appended and verified at the receiver.

## Multiple access

| Protocol | Idea | Collisions |
|:---|:---|:---|
| Channel partitioning | TDMA/FDMA/CDMA | none |
| Random access | ALOHA, CSMA, CSMA/CD, CSMA/CA | possible |
| Taking turns | polling, token passing | none |

## Ethernet

- 48-bit MAC addresses; frame: preamble, addresses, type, payload, FCS.
- Switches learn MAC→port and forward frames selectively.

## Wireless (802.11)

- CSMA/CA with ACKs and optional RTS/CTS; hidden-terminal problem.
