# factorial.s -- 5! = 120; exit status = 120.
    .text
    .globl _start
_start:
    mov $5, %rcx
    mov $1, %rax
loop:
    imul %rcx, %rax
    dec %rcx
    jnz loop
    mov %rax, %rdi
    mov $60, %rax
    syscall
