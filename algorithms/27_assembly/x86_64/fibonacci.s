# fibonacci.s -- iterative Fibonacci; exit status = fib(10) = 55.
    .text
    .globl _start
_start:
    mov $10, %rcx
    xor %rax, %rax          # f0 = 0
    mov $1, %rbx            # f1 = 1
loop:
    test %rcx, %rcx
    je done
    mov %rbx, %rdx
    add %rax, %rbx          # f1 = f0 + f1
    mov %rdx, %rax          # f0 = old f1
    dec %rcx
    jmp loop
done:
    mov %rax, %rdi          # fib(10) = 55
    mov $60, %rax
    syscall
