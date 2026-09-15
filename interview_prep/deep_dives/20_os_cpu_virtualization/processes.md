# Processes

A process is a running program plus its execution state: address space,
registers, program counter, stack, and open resources.

## Process anatomy

- **Text** (code), **data**, **heap** (grows up), **stack** (grows down).
- **Register context:** PC, stack pointer, general registers.
- **PCB/process control block:** kernel metadata (pid, state, page tables,
  file descriptors, scheduling info).

## States

`New → Ready → Running → Blocked → Ready → ... → Terminated`

## Context switch

Save the running process's registers and page-table base, switch stacks, restore
the next process. It is pure overhead but enables the CPU illusion.

## The process API

`fork`, `exec`, `wait`, `exit`; signals and pipes for coordination.

## Linux internals

`task_struct`, `clone()` for threads vs processes, cgroups and namespaces for
containers.
