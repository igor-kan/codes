# cat.s -- copy stdin to stdout using raw read/write syscalls.
    .section .bss
    .align 16
buf:
    .skip 4096

    .text
    .globl _start
_start:
read_loop:
    xor %rax, %rax          # __NR_read
    xor %rdi, %rdi          # fd 0 = stdin
    lea buf(%rip), %rsi
    mov $4096, %rdx
    syscall

    test %rax, %rax
    jle done                # EOF or error

    mov %rax, %rdx          # bytes read
    mov $1, %rax            # __NR_write
    mov $1, %rdi            # fd 1 = stdout
    lea buf(%rip), %rsi
    syscall
    jmp read_loop

done:
    mov $60, %rax
    xor %rdi, %rdi
    syscall
