# memset.s -- fill a buffer with a byte value; exit status = filler byte.
    .section .bss
    .align 16
buf:
    .skip 16

    .text
    .globl _start
# void *memset(void *rdi, int esi, size_t rdx)
memset:
    xor %rax, %rax
1:
    cmp %rdx, %rax
    jge 2f
    movb %sil, (%rdi, %rax)
    inc %rax
    jmp 1b
2:
    mov %rdi, %rax
    ret

_start:
    lea buf(%rip), %rdi
    mov $0x7f, %esi
    mov $16, %rdx
    call memset
    lea buf(%rip), %rdi
    movzbl (%rdi), %edi     # 0x7f
    mov $60, %rax
    syscall
