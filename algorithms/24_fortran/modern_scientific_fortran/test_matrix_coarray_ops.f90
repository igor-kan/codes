program test_matrix_coarray_ops
    use, intrinsic :: iso_fortran_env, only: real64, int32
    use matrix_coarray_ops_mod, only: frobenius_norm, trace_matrix, mat_transpose, blocked_matmul
    implicit none

    real(real64), dimension(2, 2) :: A, B, C
    real(real64) :: fn, tr

    A = reshape([1.0_real64, 2.0_real64, 3.0_real64, 4.0_real64], [2, 2])
    B = reshape([2.0_real64, 0.0_real64, 1.0_real64, 2.0_real64], [2, 2])

    fn = frobenius_norm(A) ! sqrt(1 + 4 + 9 + 16) = sqrt(30)
    tr = trace_matrix(A)   ! 1 + 4 = 5
    C = blocked_matmul(A, B)

    if (abs(fn - sqrt(30.0_real64)) > 1.0e-12_real64 .or. abs(tr - 5.0_real64) > 1.0e-12_real64) then
        write(*,*) "FAIL: Matrix operations norm or trace incorrect"
        stop 1
    else
        write(*,*) "PASS: Matrix operations verified"
    end if
end program test_matrix_coarray_ops
