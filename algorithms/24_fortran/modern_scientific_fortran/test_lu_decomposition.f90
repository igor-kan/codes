program test_lu_decomposition
    use, intrinsic :: iso_fortran_env, only: real64, int32
    use lu_decomposition_mod, only: lu_factor, lu_solve
    implicit none

    integer(int32), parameter :: n = 3
    real(real64), dimension(n, n) :: A, A_orig
    real(real64), dimension(n) :: b, x
    integer(int32), dimension(n) :: piv
    integer(int32) :: info
    real(real64) :: res

    A = reshape([2.0_real64, 4.0_real64, -2.0_real64, &
                 1.0_real64, -6.0_real64, 7.0_real64, &
                 -1.0_real64, 2.0_real64, 2.0_real64], [n, n])
    A_orig = A
    b = [1.0_real64, 2.0_real64, 3.0_real64]

    call lu_factor(A, piv, n, info)
    if (info /= 0) then
        write(*,*) "FAIL: LU factorization failed, info=", info
        stop 1
    end if

    call lu_solve(A, piv, b, x, n)
    res = maxval(abs(matmul(A_orig, x) - b))

    if (res > 1.0e-12_real64) then
        write(*,*) "FAIL: LU solver residual too high:", res
        stop 1
    else
        write(*,*) "PASS: LU solver residual:", res
    end if
end program test_lu_decomposition
