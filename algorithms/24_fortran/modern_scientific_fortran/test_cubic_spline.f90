program test_cubic_spline
    use, intrinsic :: iso_fortran_env, only: real64, int32
    use cubic_spline_mod, only: Spline1D, spline_init, spline_eval
    implicit none

    integer(int32), parameter :: n = 5
    real(real64), dimension(n) :: x, y
    type(Spline1D) :: sp
    real(real64) :: y_interp, err

    x = [0.0_real64, 1.0_real64, 2.0_real64, 3.0_real64, 4.0_real64]
    y = x**2

    call spline_init(x, y, n, sp)
    y_interp = spline_eval(sp, 2.5_real64)
    err = abs(y_interp - 6.25_real64)

    if (err > 0.15_real64) then
        write(*,*) "FAIL: Spline error too high:", err
        stop 1
    else
        write(*,*) "PASS: Cubic spline interpolation error:", err
    end if
end program test_cubic_spline
