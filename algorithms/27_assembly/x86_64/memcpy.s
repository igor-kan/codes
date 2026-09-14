# memcpy.s -- a byte-at-a-time memcpy; exit status = copied byte.
    .section .rodata
src:
    .ascii "ABCDEFGH"

    .section .bss
    .align 16
dst:
    .skip 8

    .text
    .globl _start
# void *memcpy(void *rdi, const void *rsi, size_t rdx)
memcpy:
    xor %rax, %rax
1:
    cmp %rdx, %rax
    jge 2f
    movzbl (%rsi, %rax), %ecx
    movb %cl, (%rdi, %rax)
    inc %rax
    jmp 1b
2:
    mov %rdi, %rax
    ret

_start:
    lea dst(%rip), %rdi
    lea src(%rip), %rsi
    mov $8, %rdx
    call memcpy
    lea dst(%rip), %rdi
    movzbl (%rdi), %edi     # 'A' = 65
    mov $60, %rax
    syscall
