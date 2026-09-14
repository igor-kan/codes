# atoi.s -- parse a decimal string; exit status = value & 0xff.
    .section .rodata
num:
    .asciz "1234"

    .text
    .globl _start
# long atoi(const char *rdi) -> rax
atoi:
    xor %rax, %rax
    xor %rcx, %rcx
1:
    movzbl (%rdi, %rcx), %edx
    test %edx, %edx
    je 2f
    sub $'0', %edx
    imul $10, %rax, %rax
    add %rdx, %rax
    inc %rcx
    jmp 1b
2:
    ret

_start:
    lea num(%rip), %rdi
    call atoi
    mov %rax, %rdi          # 1234 & 0xff = 210
    mov $60, %rax
    syscall
