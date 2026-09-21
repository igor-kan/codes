! Modern Fortran 2018 Natural Cubic Spline Interpolation
module cubic_spline_mod
    use, intrinsic :: iso_fortran_env, only: real64, int32
    implicit none
    private
    public :: Spline1D, spline_init, spline_eval

    type :: Spline1D
        integer(int32) :: n
        real(real64), allocatable :: x(:)
        real(real64), allocatable :: y(:)
        real(real64), allocatable :: y2(:)
    end type Spline1D

contains

    subroutine spline_init(x, y, n, sp)
        integer(int32), intent(in) :: n
        real(real64), dimension(n), intent(in) :: x, y
        type(Spline1D), intent(out) :: sp

        real(real64), dimension(n) :: u
        real(real64) :: sig, p
        integer(int32) :: i, k

        sp%n = n
        allocate(sp%x(n), sp%y(n), sp%y2(n))
        sp%x = x
        sp%y = y

        sp%y2(1) = 0.0_real64
        u(1) = 0.0_real64

        do i = 2, n - 1
            sig = (x(i) - x(i - 1)) / (x(i + 1) - x(i - 1))
            p = sig * sp%y2(i - 1) + 2.0_real64
            sp%y2(i) = (sig - 1.0_real64) / p
            u(i) = (6.0_real64 * ((y(i + 1) - y(i)) / (x(i + 1) - x(i)) - &
                   (y(i) - y(i - 1)) / (x(i) - x(i - 1))) / (x(i + 1) - x(i - 1)) - sig * u(i - 1)) / p
        end do

        sp%y2(n) = 0.0_real64
        do k = n - 1, 1, -1
            sp%y2(k) = sp%y2(k) * sp%y2(k + 1) + u(k)
        end do
    end subroutine spline_init

    pure function spline_eval(sp, x_val) result(y_val)
        type(Spline1D), intent(in) :: sp
        real(real64), intent(in) :: x_val
        real(real64) :: y_val

        integer(int32) :: klo, khi, k
        real(real64) :: h, a, b

        klo = 1
        khi = sp%n
        do while (khi - klo > 1)
            k = (khi + klo) / 2
            if (sp%x(k) > x_val) then
                khi = k
            else
                klo = k
            end if
        end do

        h = sp%x(khi) - sp%x(klo)
        a = (sp%x(khi) - x_val) / h
        b = (x_val - sp%x(klo)) / h
        y_val = a * sp%y(klo) + b * sp%y(khi) + &
                ((a**3 - a) * sp%y2(klo) + (b**3 - b) * sp%y2(khi)) * (h**2) / 6.0_real64
    end function spline_eval

end module cubic_spline_mod
