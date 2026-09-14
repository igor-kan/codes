# hello_world.s -- write(2) a string to stdout, then exit(0).
# Build:  as --64 hello_world.s -o hello_world.o && ld hello_world.o -o hello_world
    .section .rodata
msg:
    .ascii "Hello, World!\n"
    .set msg_len, . - msg

    .text
    .globl _start
_start:
    mov $1, %rax            # __NR_write
    mov $1, %rdi            # fd 1 = stdout
    lea msg(%rip), %rsi     # buffer
    mov $msg_len, %rdx      # count
    syscall

    mov $60, %rax           # __NR_exit
    xor %rdi, %rdi          # status 0
    syscall
