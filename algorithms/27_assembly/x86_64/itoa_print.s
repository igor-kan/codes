# itoa_print.s -- print a positive integer using syscalls only.
    .section .rodata
nl:
    .ascii "\n"

    .section .bss
    .align 16
buf:
    .skip 32

    .text
    .globl _start
# void print_uint(unsigned long rdi)
print_uint:
    lea buf+31(%rip), %rsi
    mov %rdi, %rax
    mov $10, %r8
    xor %r9, %r9            # length
    test %rax, %rax
    jne 1f
    dec %rsi
    movb $'0', (%rsi)
    inc %r9
    jmp 3f
1:
    xor %rdx, %rdx
    div %r8                 # rax = quotient, rdx = remainder
    add $'0', %dl
    dec %rsi
    mov %dl, (%rsi)
    inc %r9
    test %rax, %rax
    jne 1b
3:
    mov $1, %rax
    mov $1, %rdi
    mov %r9, %rdx
    syscall
    mov $1, %rax
    mov $1, %rdi
    lea nl(%rip), %rsi
    mov $1, %rdx
    syscall
    ret

_start:
    mov $12345, %rdi
    call print_uint
    mov $60, %rax
    xor %rdi, %rdi
    syscall
