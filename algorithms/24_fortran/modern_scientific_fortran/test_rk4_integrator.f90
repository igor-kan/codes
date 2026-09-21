program test_rk4_integrator
    use, intrinsic :: iso_fortran_env, only: real64, int32
    use rk4_integrator_mod, only: rk4_integrate, rhs_interface
    implicit none

    real(real64), dimension(1) :: y0
    real(real64) :: t0, tf, exact_final, err
    integer(int32), parameter :: n_steps = 100
    real(real64), dimension(n_steps + 1) :: t_out
    real(real64), dimension(1, n_steps + 1) :: y_out

    t0 = 0.0_real64
    tf = 2.0_real64
    y0(1) = 1.0_real64

    call rk4_integrate(t0, tf, y0, n_steps, decay_rhs, t_out, y_out)
    exact_final = exp(-tf)
    err = abs(y_out(1, n_steps + 1) - exact_final)

    if (err > 1.0e-7_real64) then
        write(*,*) "FAIL: RK4 decay error too large:", err
        stop 1
    else
        write(*,*) "PASS: RK4 integrator accurate to within", err
    end if

contains

    pure function decay_rhs(t, y) result(dydt)
        real(real64), intent(in) :: t
        real(real64), dimension(:), intent(in) :: y
        real(real64), dimension(size(y)) :: dydt
        dydt(1) = -y(1)
    end function decay_rhs

end program test_rk4_integrator
