# cpuid_vendor.s -- print the 12-byte CPU vendor string via CPUID.
    .section .bss
    .align 16
vendor:
    .skip 12

    .text
    .globl _start
_start:
    mov $0, %eax            # leaf 0: vendor id
    cpuid
    lea vendor(%rip), %r8
    mov %ebx, 0(%r8)
    mov %edx, 4(%r8)
    mov %ecx, 8(%r8)

    mov $1, %rax
    mov $1, %rdi
    mov %r8, %rsi
    mov $12, %rdx
    syscall

    mov $60, %rax
    xor %rdi, %rdi
    syscall
