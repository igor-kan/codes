program test_monte_carlo_integration
    use, intrinsic :: iso_fortran_env, only: real64, int32
    use monte_carlo_integration_mod, only: mc_integrate_sphere_volume
    implicit none

    real(real64) :: vol, std_err, exact_vol
    real(real64), parameter :: PI = 3.14159265358979323846264338327950288_real64

    exact_vol = 4.0_real64 * PI / 3.0_real64
    call mc_integrate_sphere_volume(100000, 42, vol, std_err)

    if (abs(vol - exact_vol) > 3.0_real64 * std_err + 0.05_real64) then
        write(*,*) "FAIL: MC sphere volume outside 3-sigma bound:", vol, exact_vol
        stop 1
    else
        write(*,*) "PASS: MC sphere volume:", vol, "exact:", exact_vol, "std_err:", std_err
    end if
end program test_monte_carlo_integration
