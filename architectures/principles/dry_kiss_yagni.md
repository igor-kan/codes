# DRY, KISS, YAGNI

**DRY (Don't Repeat Yourself):** every piece of *knowledge* should have a single,
authoritative representation. Do not confuse this with "avoid similar-looking
code": two blocks can look alike but change for different reasons. Deduplicate
knowledge, not text.

**KISS (Keep It Simple):** prefer the simplest design that meets the
requirement. Complexity is a cost paid on every future change.

**YAGNI (You Aren't Gonna Need It):** do not build speculative generality.
Add extension points when a second real use case appears, not before.

## Heuristics

- Rule of three before extracting an abstraction.
- If a "reusable" utility has one caller and one configuration, inline it.
- Optimize for the reader and for deletability.
- Prefer boring, well-understood technology.

**Tension:** DRY can conflict with SRP (over-merging) and with KISS (premature
abstraction). Resolve toward *change locality*: related changes should touch one
place.

Related: SOLID, Separation of Concerns, Refactoring.
