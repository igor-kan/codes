# Security Policy

## Supported versions

This repository is a collection of educational code examples. It is maintained on
the `main` branch; there are no versioned releases with security support.

## Reporting a vulnerability

If you find a security issue in any example (for example a command injection in a
script, an unsafe deserialization pattern, or a Docker/CI configuration that
leaks credentials), please report it privately:

1. Do **not** open a public issue for the vulnerability.
2. Use GitHub's **Private vulnerability reporting** (Security → Report a
   vulnerability) on this repository, or email the maintainer at the address on
   the GitHub profile `@igor-kan`.
3. Include a description, affected path(s), and a minimal reproduction if
   possible.

You can expect an acknowledgement within a few days and a fix or mitigation
plan for confirmed issues.

## Scope

- **In scope:** the example code and configuration in this repository.
- **Out of scope:** vulnerabilities in upstream projects vendored under
  `languages/` (report those upstream), and third-party dependencies.

## Handling secrets

Example configurations use placeholder credentials (for example
`replace-me`, `secret`). Never commit real secrets; use environment variables or
a secret manager. If a secret is committed accidentally, rotate it immediately
and report the incident.
