# strlen.s -- compute the length of a C string; exit status = length.
    .section .rodata
s:
    .asciz "Hello"

    .text
    .globl _start
# size_t strlen(const char *rdi) -> rax
strlen:
    xor %rax, %rax
1:
    cmpb $0, (%rdi, %rax)
    je 2f
    inc %rax
    jmp 1b
2:
    ret

_start:
    lea s(%rip), %rdi
    call strlen
    mov %rax, %rdi          # status = strlen
    mov $60, %rax
    syscall
