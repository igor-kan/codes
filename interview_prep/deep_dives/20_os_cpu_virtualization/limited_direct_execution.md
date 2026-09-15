# Limited Direct Execution

Run user code directly on the CPU for speed, but limit what it can do.

## User vs kernel mode

- **User mode:** restricted instructions fault (privileged operations).
- **Kernel mode:** full access; entered via a **trap** or interrupt.

## Traps and system calls

A syscall instruction switches to kernel mode, dispatches via a syscall table,
then returns with `return-from-trap`. The kernel validates arguments and copies
data across the boundary.

## Timer interrupt

The OS programs a timer; on expiry, control returns to the kernel, which may
invoke the scheduler. This is how the OS regains control from a runaway process.

## Cooperative vs preemptive

- **Cooperative:** process yields voluntarily (risky).
- **Preemptive:** timer-driven (modern default).

## Protection mechanisms

Page-table permissions, privilege levels, and address-space isolation prevent
one process from corrupting another or the kernel.
