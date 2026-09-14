# binary_search.s -- classic iterative binary search; exit status = index.
    .section .rodata
arr:
    .long 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
    .set arr_len, (. - arr) / 4
target:
    .long 13

    .text
    .globl _start
_start:
    lea arr(%rip), %rdi
    mov $arr_len, %rcx
    mov target(%rip), %edx
    xor %r8, %r8            # lo
    mov %rcx, %r9           # hi
loop:
    cmp %r9, %r8
    jge not_found
    mov %r8, %r10
    add %r9, %r10
    shr $1, %r10            # mid
    mov (%rdi, %r10, 4), %eax
    cmp %edx, %eax
    je found
    jl go_right
    mov %r10, %r9
    jmp loop
go_right:
    lea 1(%r10), %r8
    jmp loop
found:
    mov %r10, %rdi          # index 5
    mov $60, %rax
    syscall
not_found:
    mov $255, %rdi
    mov $60, %rax
    syscall
