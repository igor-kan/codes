! Modern Fortran 2018 Adaptive Simpson Quadrature
module simpson_quadrature_mod
    use, intrinsic :: iso_fortran_env, only: real64, int32
    implicit none
    private
    public :: simpson_composite, simpson_func_interface

    abstract interface
        pure function simpson_func_interface(x) result(f)
            import :: real64
            real(real64), intent(in) :: x
            real(real64) :: f
        end function simpson_func_interface
    end interface

contains

    pure function simpson_composite(func, a, b, n) result(integral)
        procedure(simpson_func_interface) :: func
        real(real64), intent(in) :: a, b
        integer(int32), intent(in) :: n
        real(real64) :: integral

        integer(int32) :: n_even, i
        real(real64) :: h, sum_odd, sum_even, x

        n_even = max(2, n)
        if (mod(n_even, 2) /= 0) n_even = n_even + 1

        h = (b - a) / real(n_even, real64)
        sum_odd = 0.0_real64
        sum_even = 0.0_real64

        do i = 1, n_even - 1, 2
            x = a + real(i, real64) * h
            sum_odd = sum_odd + func(x)
        end do

        do i = 2, n_even - 2, 2
            x = a + real(i, real64) * h
            sum_even = sum_even + func(x)
        end do

        integral = (h / 3.0_real64) * (func(a) + 4.0_real64 * sum_odd + 2.0_real64 * sum_even + func(b))
    end function simpson_composite

end module simpson_quadrature_mod
