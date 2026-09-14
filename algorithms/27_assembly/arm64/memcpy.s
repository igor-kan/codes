# memcpy.s -- byte copy; exit status = first copied byte ('A' = 65).
    .section .rodata
src:
    .ascii "ABCDEFGH"

    .section .bss
    .align 4
dst:
    .skip 8

    .text
    .globl _start
_start:
    adrp x0, src
    add x0, x0, :lo12:src
    adrp x1, dst
    add x1, x1, :lo12:dst
    mov x2, #0
loop:
    cmp x2, #8
    b.ge done
    ldrb w3, [x0, x2]
    strb w3, [x1, x2]
    add x2, x2, #1
    b loop
done:
    ldrb w0, [x1]
    mov x8, #93
    svc #0
