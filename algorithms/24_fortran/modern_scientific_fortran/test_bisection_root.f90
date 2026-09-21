program test_bisection_root
    use, intrinsic :: iso_fortran_env, only: real64, int32
    use bisection_root_mod, only: bisection, root_func_interface
    implicit none

    real(real64) :: root, err
    integer(int32) :: iters, status

    call bisection(poly_func, 1.0_real64, 2.0_real64, 1.0e-10_real64, 100, root, iters, status)

    ! f(x) = x^3 - x - 2, root approx 1.5213797068
    err = abs(poly_func(root))

    if (err > 1.0e-9_real64) then
        write(*,*) "FAIL: Bisection residual too large:", err
        stop 1
    else
        write(*,*) "PASS: Bisection found root:", root, "in", iters, "iterations"
    end if

contains

    pure function poly_func(x) result(f)
        real(real64), intent(in) :: x
        real(real64) :: f
        f = x**3 - x - 2.0_real64
    end function poly_func

end program test_bisection_root
