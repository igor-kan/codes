program test_cholesky_factorization
    use, intrinsic :: iso_fortran_env, only: real64, int32
    use cholesky_factorization_mod, only: cholesky_decompose, cholesky_solve
    implicit none

    integer(int32), parameter :: n = 3
    real(real64), dimension(n, n) :: A, L, LLt
    real(real64), dimension(n) :: b, x
    integer(int32) :: info
    real(real64) :: err

    A = reshape([4.0_real64, 12.0_real64, -16.0_real64, &
                 12.0_real64, 37.0_real64, -43.0_real64, &
                 -16.0_real64, -43.0_real64, 98.0_real64], [n, n])

    call cholesky_decompose(A, L, n, info)
    if (info /= 0) then
        write(*,*) "FAIL: Cholesky decomposition failed, info=", info
        stop 1
    end if

    LLt = matmul(L, transpose(L))
    err = maxval(abs(LLt - A))

    if (err > 1.0e-12_real64) then
        write(*,*) "FAIL: L L^T /= A error:", err
        stop 1
    else
        write(*,*) "PASS: Cholesky factorization verified, max error:", err
    end if
end program test_cholesky_factorization
