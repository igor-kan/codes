program test_conjugate_gradient
    use, intrinsic :: iso_fortran_env, only: real64, int32
    use conjugate_gradient_mod, only: cg_solve
    implicit none

    integer(int32), parameter :: n = 3
    real(real64), dimension(n, n) :: A
    real(real64), dimension(n) :: b, x, x_exact
    integer(int32) :: iters
    real(real64) :: res_norm

    A = reshape([4.0_real64, 1.0_real64, 0.0_real64, &
                 1.0_real64, 3.0_real64, 1.0_real64, &
                 0.0_real64, 1.0_real64, 2.0_real64], [n, n])
    x_exact = [1.0_real64, 2.0_real64, 3.0_real64]
    b = matmul(A, x_exact)

    x = 0.0_real64
    call cg_solve(A, b, x, n, 100, 1.0e-10_real64, iters, res_norm)

    if (maxval(abs(x - x_exact)) > 1.0e-8_real64) then
        write(*,*) "FAIL: CG solution error too high:", maxval(abs(x - x_exact))
        stop 1
    else
        write(*,*) "PASS: CG solver converged in", iters, "iterations, res_norm:", res_norm
    end if
end program test_conjugate_gradient
