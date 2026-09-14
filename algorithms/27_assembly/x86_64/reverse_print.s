# reverse_print.s -- print a string backwards.
    .section .rodata
msg:
    .ascii "Hello"
    .set msg_len, . - msg

    .text
    .globl _start
_start:
    lea msg+msg_len-1(%rip), %rsi
    mov $msg_len, %rdx
    mov $1, %rax
    mov $1, %rdi
syscall_write:
    # print one byte at a time, moving backwards
    push %rsi
    push %rdx
    mov $1, %rdx
    syscall
    pop %rdx
    pop %rsi
    dec %rsi
    dec %rdx
    jnz syscall_write

    mov $60, %rax
    xor %rdi, %rdi
    syscall
