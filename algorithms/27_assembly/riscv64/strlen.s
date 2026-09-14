# strlen.s -- return the length of a C string; exit status = length.
    .section .rodata
s:
    .asciz "Hello"
    .text
    .globl _start
_start:
    la a0, s
    li a1, 0
loop:
    add t0, a0, a1
    lbu t1, 0(t0)
    beqz t1, done
    addi a1, a1, 1
    j loop
done:
    mv a0, a1
    li a7, 93
    ecall
