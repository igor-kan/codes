# is_prime.s -- trial division; exit status 0 if 97 is prime, 1 otherwise.
    .text
    .globl _start
_start:
    mov $97, %rbx           # n
    cmp $2, %rbx
    jl not_prime
    mov $2, %rcx
loop:
    mov %rcx, %r8
    imul %rcx, %r8
    cmp %rbx, %r8           # while i*i <= n
    jg prime
    mov %rbx, %rax
    xor %rdx, %rdx
    div %rcx                # rdx = n % i
    test %rdx, %rdx
    je not_prime
    inc %rcx
    jmp loop
prime:
    xor %rdi, %rdi
    mov $60, %rax
    syscall
not_prime:
    mov $1, %rdi
    mov $60, %rax
    syscall
