! Modern Fortran 2018 Multi-dimensional Monte Carlo Integrator
module monte_carlo_integration_mod
    use, intrinsic :: iso_fortran_env, only: real64, int32
    implicit none
    private
    public :: mc_integrate_sphere_volume

contains

    subroutine mc_integrate_sphere_volume(n_samples, seed_val, vol, std_err)
        integer(int32), intent(in) :: n_samples, seed_val
        real(real64), intent(out) :: vol, std_err

        integer(int32) :: i, inside_count
        real(real64) :: x, y, z, p
        integer(int32), dimension(8) :: seed_arr

        seed_arr = seed_val
        call random_seed(put=seed_arr)

        inside_count = 0
        do i = 1, n_samples
            call random_number(x)
            call random_number(y)
            call random_number(z)
            ! map from [0,1] to [-1,1]
            x = 2.0_real64 * x - 1.0_real64
            y = 2.0_real64 * y - 1.0_real64
            z = 2.0_real64 * z - 1.0_real64

            if (x*x + y*y + z*z <= 1.0_real64) then
                inside_count = inside_count + 1
            end if
        end do

        p = real(inside_count, real64) / real(n_samples, real64)
        ! Box volume is 2*2*2 = 8.0
        vol = 8.0_real64 * p
        std_err = 8.0_real64 * sqrt(p * (1.0_real64 - p) / real(n_samples, real64))
    end subroutine mc_integrate_sphere_volume

end module monte_carlo_integration_mod
