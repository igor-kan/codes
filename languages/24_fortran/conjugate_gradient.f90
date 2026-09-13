! Modern Fortran 2008 Krylov Subspace Conjugate Gradient Iterative Solver.
!
! Why Fortran for this module?
! Fortran remains unbeatable in raw supercomputing linear algebra efficiency,
! column-major memory layout, native multidimensional array slicing, and zero pointer aliasing.

module conjugate_gradient_module
    use iso_fortran_env, only: real64
    implicit none
    private
    public :: solve_cg

contains

    subroutine solve_cg(A, b, x, n, tol, max_iter, iter_out)
        integer, intent(in) :: n, max_iter
        real(real64), dimension(n, n), intent(in) :: A
        real(real64), dimension(n), intent(in) :: b
        real(real64), dimension(n), intent(out) :: x
        real(real64), intent(in) :: tol
        integer, intent(out) :: iter_out

        real(real64), dimension(n) :: r, p, Ap
        real(real64) :: alpha, beta, rsold, rsnew
        integer :: k

        ! Initial guess x = 0
        x = 0.0_real64
        r = b - matmul(A, x)
        p = r
        rsold = dot_product(r, r)

        do k = 1, max_iter
            if (sqrt(rsold) < tol) exit
            Ap = matmul(A, p)
            alpha = rsold / dot_product(p, Ap)
            x = x + alpha * p
            r = r - alpha * Ap
            rsnew = dot_product(r, r)
            beta = rsnew / rsold
            p = r + beta * p
            rsold = rsnew
        end do

        iter_out = k - 1
    end subroutine solve_cg

end module conjugate_gradient_module

program test_cg
    use iso_fortran_env, only: real64
    use conjugate_gradient_module
    implicit none

    integer, parameter :: n = 3
    real(real64), dimension(n, n) :: A
    real(real64), dimension(n) :: b, x
    integer :: iters

    ! Symmetric positive-definite matrix
    A = reshape([4.0_real64, 1.0_real64, 0.0_real64, &
                 1.0_real64, 3.0_real64, 1.0_real64, &
                 0.0_real64, 1.0_real64, 2.0_real64], [n, n])
    b = [1.0_real64, 2.0_real64, 3.0_real64]

    call solve_cg(A, b, x, n, 1.0e-6_real64, 100, iters)
    print *, "Fortran 2008 CG Solver converged in iterations:", iters
    print *, "Solution vector x:", x
end program test_cg
