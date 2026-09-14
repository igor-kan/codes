# fibonacci.s -- iterative Fibonacci; exit status = fib(10) = 55.
    .text
    .globl _start
_start:
    li a0, 0                    # f0
    li a1, 1                    # f1
    li a2, 10
loop:
    beqz a2, done
    add a3, a0, a1
    mv a0, a1
    mv a1, a3
    addi a2, a2, -1
    j loop
done:
    li a7, 93
    ecall
