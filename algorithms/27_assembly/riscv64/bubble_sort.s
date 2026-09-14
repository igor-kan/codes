# bubble_sort.s -- in-place bubble sort; exit status = smallest element.
    .section .data
arr:
    .word 5, 1, 4, 2, 8, 3
    .set arr_len, (. - arr) / 4
    .text
    .globl _start
_start:
    la a0, arr
    li a1, 6                    # arr_len
    addi a1, a1, -1             # outer bound
outer:
    beqz a1, done
    li a2, 0                    # inner index
inner:
    addi a3, a2, 1
    bge a3, a1, next_outer
    slli a4, a2, 2
    add a4, a0, a4
    lw a5, 0(a4)
    lw a6, 4(a4)
    ble a5, a6, no_swap
    sw a6, 0(a4)
    sw a5, 4(a4)
no_swap:
    addi a2, a2, 1
    j inner
next_outer:
    addi a1, a1, -1
    j outer
done:
    lw a0, 0(a0)
    li a7, 93
    ecall
