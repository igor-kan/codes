# hello_world.s -- AArch64 Linux: write a string, then exit.
# Build:  clang --target=aarch64-linux-gnu -c hello_world.s -o hello_world.o
    .section .rodata
msg:
    .ascii "Hello, ARM64!\n"
    .set msg_len, . - msg

    .text
    .globl _start
_start:
    mov x0, #1                  // fd = stdout
    adrp x1, msg
    add x1, x1, :lo12:msg
    mov x2, #msg_len
    mov x8, #64                 // __NR_write
    svc #0

    mov x0, #0
    mov x8, #93                 // __NR_exit
    svc #0
