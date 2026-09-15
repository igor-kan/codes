# Email: SMTP, POP3, IMAP

## Sending with SMTP

1. Client connects (port 587 with STARTTLS, or 465 implicit TLS).
2. `EHLO`, `AUTH`, `MAIL FROM`, `RCPT TO`, `DATA`, `.`, `QUIT`.
3. Message format: headers (`From`, `To`, `Subject`, `Date`, `Message-ID`) and a
   MIME body (text, HTML, attachments).

## Retrieving mail

- **POP3:** download and typically delete from the server.
- **IMAP:** server-side folders and flags; supports multiple clients.

## Deliverability and security

- **SPF** (authorized senders), **DKIM** (signed headers), **DMARC** (policy).
- Avoid open relays; monitor reputation and bounce rates.
- TLS in transit; encryption at rest and opportunistic end-to-end (PGP/S/MIME).

## Push

IMAP IDLE or vendor push notifications deliver new mail promptly.
