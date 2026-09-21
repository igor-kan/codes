! Modern Fortran 2018 Golden Section Search 1D Optimization
module golden_section_search_mod
    use, intrinsic :: iso_fortran_env, only: real64, int32
    implicit none
    private
    public :: golden_search, opt_func_interface

    real(real64), parameter :: PHI_INV = 0.618033988749894848204586834365638_real64

    abstract interface
        pure function opt_func_interface(x) result(f)
            import :: real64
            real(real64), intent(in) :: x
            real(real64) :: f
        end function opt_func_interface
    end interface

contains

    subroutine golden_search(func, a_in, b_in, tol, max_iter, x_min, f_min, iters)
        procedure(opt_func_interface) :: func
        real(real64), intent(in) :: a_in, b_in, tol
        integer(int32), intent(in) :: max_iter
        real(real64), intent(out) :: x_min, f_min
        integer(int32), intent(out) :: iters

        real(real64) :: a, b, c, d, fc, fd
        integer(int32) :: i

        a = a_in
        b = b_in
        c = b - PHI_INV * (b - a)
        d = a + PHI_INV * (b - a)
        fc = func(c)
        fd = func(d)

        do i = 1, max_iter
            iters = i
            if (abs(b - a) < tol) exit

            if (fc < fd) then
                b = d
                d = c
                fd = fc
                c = b - PHI_INV * (b - a)
                fc = func(c)
            else
                a = c
                c = d
                fc = fd
                d = a + PHI_INV * (b - a)
                fd = func(d)
            end if
        end do

        x_min = 0.5_real64 * (a + b)
        f_min = func(x_min)
    end subroutine golden_search

end module golden_section_search_mod
