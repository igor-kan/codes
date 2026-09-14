# rdtsc.s -- read the time-stamp counter into a memory buffer.
    .section .bss
    .align 16
stamp:
    .skip 8

    .text
    .globl _start
_start:
    lfence
    rdtsc                   # edx:eax = timestamp
    shl $32, %rdx
    or %rdx, %rax
    mov %rax, stamp(%rip)
    lfence
    mov $60, %rax
    xor %rdi, %rdi
    syscall
