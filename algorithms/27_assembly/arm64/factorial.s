# factorial.s -- 5! = 120; exit status = 120.
    .text
    .globl _start
_start:
    mov w0, #1                  // accumulator
    mov w1, #5
loop:
    mul w0, w0, w1
    sub w1, w1, #1
    cbnz w1, loop
    mov x8, #93
    svc #0
