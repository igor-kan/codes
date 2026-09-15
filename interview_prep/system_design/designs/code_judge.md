# Design: Online Code Judge

**Goal:** run untrusted submissions safely.

## Key ideas

- Queue of submissions; sandboxed runners (containers/nsjail) with limits
- Compile once, run test cases with time/memory caps
- Isolate network and filesystem; cgroup CPU/memory limits
- Scoreboard updated from result stream

## Interview checklist

- Clarify functional and non-functional requirements and scale.
- Sketch the API and data model before components.
- Back-of-the-envelope capacity (QPS, storage, bandwidth).
- Identify bottlenecks, consistency needs, and failure modes.
- Finish with trade-offs and what you would monitor.
