# intel_syntax.s -- Intel-syntax variant of hello world (GNU as directive).
    .intel_syntax noprefix
    .section .rodata
msg:
    .ascii "Hello, Intel!\n"
    .set msg_len, . - msg

    .text
    .globl _start
_start:
    mov rax, 1              # __NR_write
    mov rdi, 1              # stdout
    lea rsi, [rip + msg]
    mov rdx, msg_len
    syscall

    mov rax, 60             # __NR_exit
    xor rdi, rdi
    syscall
