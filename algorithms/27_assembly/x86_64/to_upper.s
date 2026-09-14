# to_upper.s -- convert an ASCII string to uppercase and print it.
    .section .rodata
msg:
    .ascii "hello"
    .set msg_len, . - msg

    .section .bss
    .align 16
buf:
    .skip 16

    .text
    .globl _start
_start:
    lea msg(%rip), %rsi
    lea buf(%rip), %rdi
    mov $msg_len, %rcx
    xor %r8, %r8
loop:
    movzbl (%rsi, %r8), %eax
    cmp $'a', %eax
    jl store
    cmp $'z', %eax
    jg store
    sub $32, %eax
store:
    mov %al, (%rdi, %r8)
    inc %r8
    cmp %rcx, %r8
    jl loop

    mov $1, %rax
    mov $1, %rdi
    lea buf(%rip), %rsi
    mov $msg_len, %rdx
    syscall

    mov $60, %rax
    xor %rdi, %rdi
    syscall
