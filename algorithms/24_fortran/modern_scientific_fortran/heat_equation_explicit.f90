! Modern Fortran 2018 1D Transient Heat Diffusion FTCS
module heat_equation_explicit_mod
    use, intrinsic :: iso_fortran_env, only: real64, int32
    implicit none
    private
    public :: solve_heat_1d

contains

    subroutine solve_heat_1d(alpha, dx, dt, nx, nt, u_init, u_left, u_right, u_final, stable)
        real(real64), intent(in) :: alpha, dx, dt, u_left, u_right
        integer(int32), intent(in) :: nx, nt
        real(real64), dimension(nx), intent(in) :: u_init
        real(real64), dimension(nx), intent(out) :: u_final
        logical, intent(out) :: stable

        real(real64) :: r
        real(real64), dimension(nx) :: u_old, u_new
        integer(int32) :: i, step

        r = alpha * dt / (dx**2)
        stable = (r <= 0.5_real64)

        u_old = u_init
        u_old(1) = u_left
        u_old(nx) = u_right

        do step = 1, nt
            u_new(1) = u_left
            u_new(nx) = u_right
            do i = 2, nx - 1
                u_new(i) = u_old(i) + r * (u_old(i + 1) - 2.0_real64 * u_old(i) + u_old(i - 1))
            end do
            u_old = u_new
        end do

        u_final = u_old
    end subroutine solve_heat_1d

end module heat_equation_explicit_mod
