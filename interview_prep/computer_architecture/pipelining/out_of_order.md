# Out-of-Order Execution

Execute instructions as soon as their operands are ready, not in program order,
while retiring results in order to preserve precise exceptions.

## Mechanism

1. Fetch and decode in order.
2. Rename to physical registers, allocate reorder-buffer entries.
3. Dispatch to reservation stations / issue queues.
4. Wake and select ready instructions, execute out of order.
5. Write results, broadcast tags.
6. **Retire in order** from the ROB; commit or squash on misprediction.

## Key structures

- **Reorder buffer**, **load/store queue**, **physical register file**,
  **free list**.

## Benefits and costs

- Hides memory latency, improves IPC, exploits ILP.
- High complexity, power, and area; limited by window size and dependencies.

## Related

- Memory disambiguation predicts whether loads can bypass stores.
- Speculative execution is the basis of modern high-performance cores.
