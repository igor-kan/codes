# sum_array.s -- sum an array of 32-bit ints; exit status = sum.
    .section .rodata
arr:
    .long 1, 2, 3, 4, 5
    .set arr_len, (. - arr) / 4

    .text
    .globl _start
_start:
    lea arr(%rip), %rsi
    mov $arr_len, %rcx
    xor %eax, %eax          # accumulator
    xor %r8, %r8            # index
loop:
    add (%rsi, %r8, 4), %eax
    inc %r8
    cmp %rcx, %r8
    jl loop

    mov %rax, %rdi
    mov $60, %rax
    syscall
