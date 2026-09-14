# bubble_sort.s -- in-place bubble sort; exit status = smallest element.
    .section .data
arr:
    .long 5, 1, 4, 2, 8, 3
    .set arr_len, (. - arr) / 4

    .text
    .globl _start
_start:
    lea arr(%rip), %rdi
    mov $arr_len, %rcx
    dec %rcx                # outer bound
outer:
    test %rcx, %rcx
    je done
    xor %r8, %r8
inner:
    mov %r8, %r9
    inc %r9
    cmp %rcx, %r9
    jge next_outer
    mov (%rdi, %r8, 4), %eax
    mov (%rdi, %r9, 4), %edx
    cmp %edx, %eax
    jle no_swap
    mov %edx, (%rdi, %r8, 4)
    mov %eax, (%rdi, %r9, 4)
no_swap:
    inc %r8
    jmp inner
next_outer:
    dec %rcx
    jmp outer
done:
    mov (%rdi), %edi        # arr[0] = 1
    mov $60, %rax
    syscall
