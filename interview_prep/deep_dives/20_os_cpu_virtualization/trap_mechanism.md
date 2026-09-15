# Traps, Interrupts and Exceptions

## Taxonomy

- **Interrupt:** asynchronous, external (timer, NIC).
- **Trap / syscall:** synchronous, intentional (system call).
- **Exception / fault:** synchronous, unintended (page fault, divide by zero).

## Handling flow

1. Hardware saves minimal state and switches to kernel mode.
2. Kernel dispatches to a handler via the IDT (x86) or exception vector table.
3. Handler runs; for faults it may fix (page fault) or signal (SIGSEGV).
4. `iret`/`rti` returns to user mode.

## Syscall path (x86-64 Linux)

```
mov rax, <syscall_number>
mov rdi, ...
syscall
```

The kernel validates the number and arguments, then executes the service.

## Cost

Mode switches and cache/TLB effects make syscalls expensive; batching
(io_uring) and vDSO reduce the frequency.
