program test_simpson_quadrature
    use, intrinsic :: iso_fortran_env, only: real64, int32
    use simpson_quadrature_mod, only: simpson_composite, simpson_func_interface
    implicit none

    real(real64) :: val, exact, err
    real(real64), parameter :: PI = 3.14159265358979323846264338327950288_real64

    val = simpson_composite(sin_func, 0.0_real64, PI, 100)
    exact = 2.0_real64
    err = abs(val - exact)

    if (err > 1.0e-7_real64) then
        write(*,*) "FAIL: Simpson integral error:", err
        stop 1
    else
        write(*,*) "PASS: Simpson integral sin(x) in [0, pi] = 2.0 with error:", err
    end if

contains

    pure function sin_func(x) result(f)
        real(real64), intent(in) :: x
        real(real64) :: f
        f = sin(x)
    end function sin_func

end program test_simpson_quadrature
