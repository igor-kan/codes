# sse_sum.s -- 128-bit integer addition with SSE2 (paddd).
    .section .rodata
    .align 16
a:
    .long 1, 2, 3, 4
b:
    .long 10, 20, 30, 40

    .text
    .globl _start
_start:
    movdqa a(%rip), %xmm0
    movdqa b(%rip), %xmm1
    paddd %xmm1, %xmm0      # xmm0 = {11, 22, 33, 44}
    movd %xmm0, %edi        # first lane = 11
    mov $60, %rax
    syscall
