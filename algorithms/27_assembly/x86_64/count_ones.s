# count_ones.s -- software population count (Kernighan's trick).
    .text
    .globl _start
_start:
    mov $0b10110111, %rax
    xor %rcx, %rcx
loop:
    test %rax, %rax
    je done
    lea -1(%rax), %rdx
    and %rdx, %rax          # clear the lowest set bit
    inc %rcx
    jmp loop
done:
    mov %rcx, %rdi          # 6 bits set
    mov $60, %rax
    syscall
