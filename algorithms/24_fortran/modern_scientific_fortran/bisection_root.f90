! Modern Fortran 2018 Robust Root Finder (Bisection & Illinois Regula Falsi)
module bisection_root_mod
    use, intrinsic :: iso_fortran_env, only: real64, int32
    implicit none
    private
    public :: bisection, root_func_interface

    abstract interface
        pure function root_func_interface(x) result(f)
            import :: real64
            real(real64), intent(in) :: x
            real(real64) :: f
        end function root_func_interface
    end interface

contains

    subroutine bisection(func, a_in, b_in, tol, max_iter, root, iters, status)
        procedure(root_func_interface) :: func
        real(real64), intent(in) :: a_in, b_in, tol
        integer(int32), intent(in) :: max_iter
        real(real64), intent(out) :: root
        integer(int32), intent(out) :: iters, status

        real(real64) :: a, b, c, fa, fb, fc
        integer(int32) :: i

        a = a_in
        b = b_in
        fa = func(a)
        fb = func(b)

        if (fa * fb > 0.0_real64) then
            status = 1
            root = a
            iters = 0
            return
        end if

        status = 0
        do i = 1, max_iter
            c = 0.5_real64 * (a + b)
            fc = func(c)
            iters = i

            if (abs(fc) < tol .or. 0.5_real64 * (b - a) < tol) then
                root = c
                return
            end if

            if (fa * fc < 0.0_real64) then
                b = c
                fb = fc
            else
                a = c
                fa = fc
            end if
        end do

        root = 0.5_real64 * (a + b)
        status = 2 ! max iterations reached
    end subroutine bisection

end module bisection_root_mod
