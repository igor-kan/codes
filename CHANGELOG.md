# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `formal_statistics/` — Lean 4 + Mathlib formalization of Kutner's regression
  analysis (Ch. 1–2): least squares, the master decomposition, `SSTO = SSR + SSE`,
  `R²`, Cauchy–Schwarz and `|r| ≤ 1`, `F = t²`.
- `formal_physics/` — Lean 4 + Mathlib formalization of Taylor's *Classical
  Mechanics* (Ch. 6, 7, 13).
- `interview_prep/deep_dives/` — numbered deep dives (C++20, STL, smart
  pointers, reimplementation, networking 15–19, OS 20–31).
- `docs/` — documentation hub (`STRUCTURE.md`, `USAGE.md`).
- Additional algorithms across C, C++, Java, Rust, Go, JavaScript, TypeScript,
  C#, Python, Julia, Ruby, PHP, Lua, Kotlin and Swift (max heap, circular
  buffer, Boyer-Moore, Catalan, egg dropping, matrix exponentiation, Gaussian
  elimination, point-in-polygon, closest pair, base64).
- `.github/workflows/validate.yml` — CI validating Python/JSON/YAML/shell and
  internal markdown links.
- Community-health files: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`,
  `SECURITY.md`, issue and pull-request templates.

## [1.0.0] - 2026-09-13

### Added
- Initial public release: `algorithms/` across 25 languages, `architectures/`,
  `scripts/`, and a sparse-checkout workflow for the large
  `languages/` upstream corpus.

[Unreleased]: https://github.com/igor-kan/codes/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/igor-kan/codes/releases/tag/v1.0.0
