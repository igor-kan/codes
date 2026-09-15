module monte_carlo_mod
  implicit none
contains
  real(8) function square(x)
    real(8), intent(in) :: x
    square = x * x
  end function square

  real(8) function monte_carlo_integration(a, b, samples)
    real(8), intent(in) :: a, b
    integer, intent(in) :: samples
    integer(8) :: state, modulus
    real(8) :: total
    integer :: i
    state = 42
    modulus = 2_8 ** 31
    total = 0d0
    do i = 1, samples
      state = mod(1103515245_8 * state + 12345_8, modulus)
      total = total + square(a + (b - a) * real(state, 8) / real(modulus, 8))
    end do
    monte_carlo_integration = (b - a) * total / samples
  end function monte_carlo_integration
end module monte_carlo_mod

program test_monte_carlo
  use monte_carlo_mod
  implicit none
  print *, "[Fortran Monte Carlo] integral =", monte_carlo_integration(0d0, 1d0, 100000)
  if (abs(monte_carlo_integration(0d0, 1d0, 100000) - 1d0 / 3d0) > 1d-2) error stop "monte carlo failed"
  print *, "[Fortran Monte Carlo] Test completed."
end program test_monte_carlo
