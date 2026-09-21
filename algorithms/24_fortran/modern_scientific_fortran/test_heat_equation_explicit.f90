program test_heat_equation_explicit
    use, intrinsic :: iso_fortran_env, only: real64, int32
    use heat_equation_explicit_mod, only: solve_heat_1d
    implicit none

    integer(int32), parameter :: nx = 51, nt = 100
    real(real64) :: alpha, dx, dt, t_final
    real(real64), dimension(nx) :: u_init, u_final, x, u_exact
    logical :: stable
    integer(int32) :: i
    real(real64) :: max_err
    real(real64), parameter :: PI = 3.14159265358979323846264338327950288_real64

    alpha = 0.01_real64
    dx = 1.0_real64 / real(nx - 1, real64)
    dt = 0.4_real64 * (dx**2) / alpha ! ensure stability r = 0.4 <= 0.5

    do i = 1, nx
        x(i) = real(i - 1, real64) * dx
        u_init(i) = sin(PI * x(i))
    end do

    call solve_heat_1d(alpha, dx, dt, nx, nt, u_init, 0.0_real64, 0.0_real64, u_final, stable)

    if (.not. stable) then
        write(*,*) "FAIL: Unstable CFL condition"
        stop 1
    end if

    t_final = real(nt, real64) * dt
    u_exact = exp(-alpha * (PI**2) * t_final) * sin(PI * x)
    max_err = maxval(abs(u_final - u_exact))

    if (max_err > 5.0e-3_real64) then
        write(*,*) "FAIL: Heat equation error too large:", max_err
        stop 1
    else
        write(*,*) "PASS: Heat equation FTCS accurate, max error:", max_err
    end if
end program test_heat_equation_explicit
