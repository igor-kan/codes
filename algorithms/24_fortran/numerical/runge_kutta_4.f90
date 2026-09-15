module rk4_mod
  implicit none
contains
  real(8) function rhs(t, y)
    real(8), intent(in) :: t, y
    rhs = y
  end function rhs

  real(8) function rk4(y0, t0, t1, steps)
    real(8), intent(in) :: y0, t0, t1
    integer, intent(in) :: steps
    real(8) :: h, y, t, k1, k2, k3, k4
    integer :: i
    h = (t1 - t0) / steps
    y = y0
    t = t0
    do i = 1, steps
      k1 = h * rhs(t, y)
      k2 = h * rhs(t + h / 2d0, y + k1 / 2d0)
      k3 = h * rhs(t + h / 2d0, y + k2 / 2d0)
      k4 = h * rhs(t + h, y + k3)
      y = y + (k1 + 2d0 * k2 + 2d0 * k3 + k4) / 6d0
      t = t + h
    end do
    rk4 = y
  end function rk4
end module rk4_mod

program test_rk4
  use rk4_mod
  implicit none
  real(8) :: value
  value = rk4(1d0, 0d0, 1d0, 1000)
  print *, "[Fortran RK4] y(1) =", value
  if (abs(value - exp(1d0)) > 1d-9) error stop "rk4 failed"
  print *, "[Fortran RK4] Test completed."
end program test_rk4
