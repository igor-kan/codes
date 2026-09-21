program test_thomas_tridiagonal
    use, intrinsic :: iso_fortran_env, only: real64, int32
    use thomas_tridiagonal_mod, only: solve_tridiagonal
    implicit none

    integer(int32), parameter :: n = 4
    real(real64), dimension(n) :: a, b, c, d, x
    integer(int32) :: status
    real(real64) :: r1, r2, r3, r4, max_res

    ! System:
    ! [ 2  -1   0   0 ] [x1]   [ 1 ]
    ! [-1   2  -1   0 ] [x2] = [ 0 ]
    ! [ 0  -1   2  -1 ] [x3]   [ 0 ]
    ! [ 0   0  -1   2 ] [x4]   [ 1 ]
    a = [0.0_real64, -1.0_real64, -1.0_real64, -1.0_real64]
    b = [2.0_real64,  2.0_real64,  2.0_real64,  2.0_real64]
    c = [-1.0_real64, -1.0_real64, -1.0_real64, 0.0_real64]
    d = [1.0_real64,  0.0_real64,  0.0_real64,  1.0_real64]

    call solve_tridiagonal(a, b, c, d, x, n, status)

    if (status /= 0) then
        write(*,*) "FAIL: Thomas solver returned nonzero status:", status
        stop 1
    end if

    ! Analytical solution is all 1s:
    r1 = abs(x(1) - 1.0_real64)
    r2 = abs(x(2) - 1.0_real64)
    r3 = abs(x(3) - 1.0_real64)
    r4 = abs(x(4) - 1.0_real64)
    max_res = max(r1, max(r2, max(r3, r4)))

    if (max_res > 1.0e-12_real64) then
        write(*,*) "FAIL: Max residual too high:", max_res
        stop 1
    else
        write(*,*) "PASS: Thomas tridiagonal solution exact, residual:", max_res
    end if
end program test_thomas_tridiagonal
