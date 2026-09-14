# sum_array.s -- sum an array of 32-bit ints; exit status = sum.
    .section .data
arr:
    .word 1, 2, 3, 4, 5
    .set arr_len, (. - arr) / 4

    .text
    .globl _start
_start:
    adrp x0, arr
    add x0, x0, :lo12:arr
    mov w1, #0                  // sum
    mov w2, #0                  // index
loop:
    cmp w2, #5                  // arr_len
    b.ge done
    ldr w3, [x0, x2, lsl #2]
    add w1, w1, w3
    add w2, w2, #1
    b loop
done:
    mov w0, w1
    mov x8, #93
    svc #0
