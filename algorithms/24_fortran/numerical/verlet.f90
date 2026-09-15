module verlet_mod
  implicit none
contains
  real(8) function acceleration(x)
    real(8), intent(in) :: x
    acceleration = -x
  end function acceleration

  subroutine verlet(x0, v0, dt, steps, xout, vout)
    real(8), intent(in) :: x0, v0, dt
    integer, intent(in) :: steps
    real(8), intent(out) :: xout, vout
    real(8) :: x, v, a, x_new, a_new
    integer :: i
    x = x0; v = v0
    do i = 1, steps
      a = acceleration(x)
      x_new = x + v * dt + 0.5d0 * a * dt * dt
      a_new = acceleration(x_new)
      v = v + 0.5d0 * (a + a_new) * dt
      x = x_new
    end do
    xout = x; vout = v
  end subroutine verlet
end module verlet_mod

program test_verlet
  use verlet_mod
  implicit none
  real(8) :: x, v, energy
  call verlet(1d0, 0d0, 1d-3, 10000, x, v)
  energy = 0.5d0 * (v * v + x * x)
  print *, "[Fortran Verlet] energy =", energy, " x =", x
  if (abs(energy - 0.5d0) > 1d-3) error stop "verlet energy failed"
  if (abs(x - cos(10d0)) > 1d-2) error stop "verlet position failed"
  print *, "[Fortran Verlet] Test completed."
end program test_verlet
