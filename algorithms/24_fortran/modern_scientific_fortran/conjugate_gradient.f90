! Modern Fortran 2018 Linear Conjugate Gradient Solver
module conjugate_gradient_mod
    use, intrinsic :: iso_fortran_env, only: real64, int32
    implicit none
    private
    public :: cg_solve

contains

    subroutine cg_solve(A, b, x, n, max_iter, tol, iters, res_norm)
        integer(int32), intent(in) :: n, max_iter
        real(real64), dimension(n, n), intent(in) :: A
        real(real64), dimension(n), intent(in) :: b
        real(real64), dimension(n), intent(inout) :: x
        real(real64), intent(in) :: tol
        integer(int32), intent(out) :: iters
        real(real64), intent(out) :: res_norm

        real(real64), dimension(n) :: r, p, Ap
        real(real64) :: rs_old, rs_new, alpha, beta
        integer(int32) :: k

        r = b - matmul(A, x)
        p = r
        rs_old = dot_product(r, r)
        iters = 0

        if (sqrt(rs_old) < tol) then
            res_norm = sqrt(rs_old)
            return
        end if

        do k = 1, max_iter
            Ap = matmul(A, p)
            alpha = rs_old / dot_product(p, Ap)
            x = x + alpha * p
            r = r - alpha * Ap
            rs_new = dot_product(r, r)
            iters = k
            res_norm = sqrt(rs_new)

            if (res_norm < tol) exit

            beta = rs_new / rs_old
            p = r + beta * p
            rs_old = rs_new
        end do
    end subroutine cg_solve

end module conjugate_gradient_mod
