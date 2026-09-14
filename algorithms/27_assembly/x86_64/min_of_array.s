# min_of_array.s -- find the minimum element; exit status = minimum.
    .section .rodata
arr:
    .long 7, 3, 9, 1, 4, 2
    .set arr_len, (. - arr) / 4

    .text
    .globl _start
_start:
    lea arr(%rip), %rsi
    mov arr(%rip), %eax     # running min
    mov $1, %r8
loop:
    mov (%rsi, %r8, 4), %edx
    cmp %eax, %edx
    jge skip
    mov %edx, %eax
skip:
    inc %r8
    cmp $arr_len, %r8
    jl loop
    mov %rax, %rdi
    mov $60, %rax
    syscall
