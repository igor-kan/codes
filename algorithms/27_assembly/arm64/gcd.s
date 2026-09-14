# gcd.s -- Euclid's algorithm; exit status = gcd(48, 36) = 12.
    .text
    .globl _start
_start:
    mov w0, #48
    mov w1, #36
loop:
    cbz w1, done
    udiv w2, w0, w1             // q = a / b
    msub w3, w2, w1, w0         // r = a - q * b
    mov w0, w1
    mov w1, w3
    b loop
done:
    mov x8, #93
    svc #0
