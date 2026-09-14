# bubble_sort.s -- in-place bubble sort; exit status = smallest element.
    .section .data
arr:
    .word 5, 1, 4, 2, 8, 3
    .set arr_len, (. - arr) / 4

    .text
    .globl _start
_start:
    adrp x0, arr
    add x0, x0, :lo12:arr
    mov w9, #arr_len
    sub w9, w9, #1              // outer bound
outer:
    cbz w9, done
    mov w8, w8                  // no-op keeps assembler quiet
    mov w2, #0
inner:
    add w3, w2, #1
    cmp w3, w9
    b.ge next_outer
    ldr w4, [x0, w2, UXTW #2]
    ldr w5, [x0, w3, UXTW #2]
    cmp w4, w5
    b.le no_swap
    str w5, [x0, w2, UXTW #2]
    str w4, [x0, w3, UXTW #2]
no_swap:
    add w2, w2, #1
    b inner
next_outer:
    sub w9, w9, #1
    b outer
done:
    ldr w0, [x0]
    mov x8, #93
    svc #0
