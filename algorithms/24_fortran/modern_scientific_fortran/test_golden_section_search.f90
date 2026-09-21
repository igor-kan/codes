program test_golden_section_search
    use, intrinsic :: iso_fortran_env, only: real64, int32
    use golden_section_search_mod, only: golden_search, opt_func_interface
    implicit none

    real(real64) :: x_min, f_min, err
    integer(int32) :: iters

    call golden_search(parabola, 0.0_real64, 5.0_real64, 1.0e-8_real64, 100, x_min, f_min, iters)
    err = abs(x_min - 3.0_real64)

    if (err > 1.0e-7_real64) then
        write(*,*) "FAIL: Minimum location error too high:", err
        stop 1
    else
        write(*,*) "PASS: Golden section search found minimum at:", x_min, "iters:", iters
    end if

contains

    pure function parabola(x) result(f)
        real(real64), intent(in) :: x
        real(real64) :: f
        f = (x - 3.0_real64)**2 + 2.0_real64
    end function parabola

end program test_golden_section_search
