# Design: Realtime Leaderboard

**Goal:** rank millions of players.

## Key ideas

- Sorted-set per leaderboard in memory; sharded by range
- Score updates via streams; periodic persistence
- Rank queries with offsets; neighborhood queries around a player
- Season resets and anti-cheat validation

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
