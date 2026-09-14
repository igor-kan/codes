# hello_world.s -- RV64 Linux: write a string, then exit.
# Build:  clang --target=riscv64-linux-gnu -c hello_world.s -o hello_world.o
    .section .rodata
msg:
    .ascii "Hello, RISC-V!\n"
    .set msg_len, . - msg

    .text
    .globl _start
_start:
    li a0, 1                    # fd = stdout
    la a1, msg
    li a2, msg_len
    li a7, 64                   # __NR_write
    ecall

    li a0, 0
    li a7, 93                   # __NR_exit
    ecall
