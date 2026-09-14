# sum_array.s -- sum an array of 32-bit ints; exit status = sum.
    .section .data
arr:
    .word 1, 2, 3, 4, 5
    .set arr_len, (. - arr) / 4

    .text
    .globl _start
_start:
    la t0, arr
    li t1, 0                    # sum
    li t2, 0                    # index
loop:
    li t3, 5                    # arr_len
    bge t2, t3, done
    slli t4, t2, 2
    add t5, t0, t4
    lw t6, 0(t5)
    add t1, t1, t6
    addi t2, t2, 1
    j loop
done:
    mv a0, t1
    li a7, 93
    ecall
