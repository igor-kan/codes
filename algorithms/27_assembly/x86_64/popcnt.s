# popcnt.s -- population count with the POPCNT instruction.
    .text
    .globl _start
_start:
    mov $0xf0f0f0f0, %eax
    popcnt %eax, %ecx       # 16 set bits
    mov %rcx, %rdi
    mov $60, %rax
    syscall
