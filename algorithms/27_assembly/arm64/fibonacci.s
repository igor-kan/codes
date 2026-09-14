# fibonacci.s -- iterative Fibonacci; exit status = fib(10) = 55.
    .text
    .globl _start
_start:
    mov w0, #0                  // f0
    mov w1, #1                  // f1
    mov w2, #10
loop:
    cbz w2, done
    add w3, w0, w1
    mov w0, w1
    mov w1, w3
    sub w2, w2, #1
    b loop
done:
    mov x8, #93
    svc #0
