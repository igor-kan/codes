# exit_42.s -- terminate the process with status code 42.
    .text
    .globl _start
_start:
    mov $60, %rax           # __NR_exit
    mov $42, %rdi           # status
    syscall
