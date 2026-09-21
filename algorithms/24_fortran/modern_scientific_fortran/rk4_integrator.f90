! Modern Fortran 2018 Runge-Kutta 4th Order Integrator
module rk4_integrator_mod
    use, intrinsic :: iso_fortran_env, only: real64, int32
    implicit none
    private
    public :: rk4_step, rk4_integrate, rhs_interface

    abstract interface
        pure function rhs_interface(t, y) result(dydt)
            import :: real64
            real(real64), intent(in) :: t
            real(real64), dimension(:), intent(in) :: y
            real(real64), dimension(size(y)) :: dydt
        end function rhs_interface
    end interface

contains

    subroutine rk4_step(t, y, dt, dydt_func, y_next)
        real(real64), intent(in) :: t, dt
        real(real64), dimension(:), intent(in) :: y
        procedure(rhs_interface) :: dydt_func
        real(real64), dimension(size(y)), intent(out) :: y_next
        
        real(real64), dimension(size(y)) :: k1, k2, k3, k4
        integer(int32) :: n
        
        n = size(y)
        k1 = dt * dydt_func(t, y)
        k2 = dt * dydt_func(t + 0.5_real64 * dt, y + 0.5_real64 * k1)
        k3 = dt * dydt_func(t + 0.5_real64 * dt, y + 0.5_real64 * k2)
        k4 = dt * dydt_func(t + dt, y + k3)
        
        y_next = y + (k1 + 2.0_real64 * k2 + 2.0_real64 * k3 + k4) / 6.0_real64
    end subroutine rk4_step

    subroutine rk4_integrate(t0, tf, y0, n_steps, dydt_func, t_out, y_out)
        real(real64), intent(in) :: t0, tf
        real(real64), dimension(:), intent(in) :: y0
        integer(int32), intent(in) :: n_steps
        procedure(rhs_interface) :: dydt_func
        real(real64), dimension(n_steps + 1), intent(out) :: t_out
        real(real64), dimension(size(y0), n_steps + 1), intent(out) :: y_out
        
        real(real64) :: dt, t_curr
        real(real64), dimension(size(y0)) :: y_curr, y_next
        integer(int32) :: i
        
        dt = (tf - t0) / real(n_steps, real64)
        t_curr = t0
        y_curr = y0
        
        t_out(1) = t_curr
        y_out(:, 1) = y_curr
        
        do i = 1, n_steps
            call rk4_step(t_curr, y_curr, dt, dydt_func, y_next)
            t_curr = t0 + real(i, real64) * dt
            y_curr = y_next
            t_out(i + 1) = t_curr
            y_out(:, i + 1) = y_curr
        end do
    end subroutine rk4_integrate

end module rk4_integrator_mod
