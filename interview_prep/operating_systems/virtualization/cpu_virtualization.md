# CPU Virtualization (OSTEP)

## The process abstraction

A process is a running program with its own address space, registers, stack and
program counter. The OS provides **isolation** and the **illusion** of a
dedicated CPU.

## Mechanisms

- **Trap:** switch from user mode to kernel mode.
- **Timer interrupt:** regains control from a runaway process.
- **Context switch:** save/restore registers and switch page tables.

## Policies (schedulers)

| Scheduler | Policy | Trade-off |
|:---|:---|:---|
| FIFO | first-in first-out | convoy effect |
| SJF | shortest job first | needs future knowledge |
| STCF | shortest time-to-completion | optimal turnaround, poor response |
| RR | round robin | good response, more context switches |
| MLFQ | multi-level feedback | learns from behavior |

Metrics: **turnaround** = completion − arrival; **response** = first run − arrival.
