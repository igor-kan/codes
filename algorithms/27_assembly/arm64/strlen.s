# strlen.s -- return the length of a C string; exit status = length.
    .section .rodata
s:
    .asciz "Hello"

    .text
    .globl _start
_start:
    adrp x0, s
    add x0, x0, :lo12:s
    mov x1, #0
loop:
    ldrb w2, [x0, x1]
    cbz w2, done
    add x1, x1, #1
    b loop
done:
    mov w0, w1
    mov x8, #93
    svc #0
