# Golden Master (Characterization) Testing

Capture current output as a reference and assert future output matches it —
useful when refactoring legacy code with no tests.

## Steps

1. Run the system on representative inputs; store outputs as golden files.
2. Add a test comparing actual to golden output.
3. Refactor; review diffs when behaviour legitimately changes.

## Caution

- Golden files can encode bugs; review and update deliberately.
- Keep inputs small and deterministic; normalize timestamps/IDs.

Related: Approval Testing, Snapshot Testing.
