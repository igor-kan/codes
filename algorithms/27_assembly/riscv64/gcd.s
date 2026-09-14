# gcd.s -- Euclid's algorithm; exit status = gcd(48, 36) = 12.
    .text
    .globl _start
_start:
    li a0, 48
    li a1, 36
loop:
    beqz a1, done
    rem a2, a0, a1
    mv a0, a1
    mv a1, a2
    j loop
done:
    li a7, 93
    ecall
