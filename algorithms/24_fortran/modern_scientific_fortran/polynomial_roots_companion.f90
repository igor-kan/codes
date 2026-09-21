! Modern Fortran 2018 Polynomial Evaluation and Newton Root Finder
module polynomial_roots_companion_mod
    use, intrinsic :: iso_fortran_env, only: real64, int32
    implicit none
    private
    public :: horner_eval, newton_poly_root

contains

    pure subroutine horner_eval(coeffs, deg, x, val, dval)
        integer(int32), intent(in) :: deg
        real(real64), dimension(deg + 1), intent(in) :: coeffs
        real(real64), intent(in) :: x
        real(real64), intent(out) :: val, dval

        integer(int32) :: i

        val = coeffs(deg + 1)
        dval = 0.0_real64

        do i = deg, 1, -1
            dval = dval * x + val
            val = val * x + coeffs(i)
        end do
    end subroutine horner_eval

    subroutine newton_poly_root(coeffs, deg, x0, tol, max_iter, root, iters, status)
        integer(int32), intent(in) :: deg, max_iter
        real(real64), dimension(deg + 1), intent(in) :: coeffs
        real(real64), intent(in) :: x0, tol
        real(real64), intent(out) :: root
        integer(int32), intent(out) :: iters, status

        real(real64) :: x, val, dval, dx
        integer(int32) :: i

        status = 0
        x = x0

        do i = 1, max_iter
            iters = i
            call horner_eval(coeffs, deg, x, val, dval)

            if (abs(val) < tol) then
                root = x
                return
            end if

            if (abs(dval) < 1.0e-15_real64) then
                status = 1 ! zero derivative
                root = x
                return
            end if

            dx = val / dval
            x = x - dx

            if (abs(dx) < tol) then
                root = x
                return
            end if
        end do

        root = x
        status = 2 ! max iters reached
    end subroutine newton_poly_root

end module polynomial_roots_companion_mod
