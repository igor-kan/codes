# gcd.s -- Euclid's algorithm; exit status = gcd(48, 36) = 12.
    .text
    .globl _start
_start:
    mov $48, %rax
    mov $36, %rbx
loop:
    test %rbx, %rbx
    je done
    xor %rdx, %rdx
    div %rbx                # rdx = rax % rbx
    mov %rbx, %rax
    mov %rdx, %rbx
    jmp loop
done:
    mov %rax, %rdi
    mov $60, %rax
    syscall
