# int_pow.s -- exponentiation by squaring; exit status = 2^5 = 32.
    .text
    .globl _start
_start:
    mov $2, %rbx            # base
    mov $5, %rcx            # exponent
    mov $1, %rax            # result
loop:
    test %rcx, %rcx
    je done
    test $1, %rcx
    jz skip_mul
    imul %rbx, %rax
skip_mul:
    imul %rbx, %rbx
    shr $1, %rcx
    jmp loop
done:
    mov %rax, %rdi
    mov $60, %rax
    syscall
