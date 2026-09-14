# Superscalar Execution

Issue and execute multiple instructions per cycle by replicating functional
units and dynamically scheduling independent instructions.

## Components

- **Instruction fetch/decode** of several instructions per cycle.
- **Register renaming** to remove WAR/WAW dependencies.
- **Reorder buffer** for speculative, out-of-order execution.
- **Reservation stations** / scheduler to pick ready instructions.
- **Functional units:** ALUs, load/store units, FP/SIMD, branch units.

## Limits

- **Instruction-level parallelism (ILP)** in the program.
- Window size and scheduler complexity.
- Memory latency and dependency chains.
- Power and area.

## Techniques

- Wide issue, deep windows, speculative execution.
- SMT (simultaneous multithreading) fills bubbles from multiple threads.
- Fusion of compare+branch, macro-ops, and micro-op caches.
