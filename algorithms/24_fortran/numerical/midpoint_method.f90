module midpoint_mod
  implicit none
contains
  real(8) function rhs(t, y)
    real(8), intent(in) :: t, y
    rhs = y
  end function rhs

  real(8) function midpoint_method(y0, t0, t1, steps)
    real(8), intent(in) :: y0, t0, t1
    integer, intent(in) :: steps
    real(8) :: h, y, t, k1, k2
    integer :: i
    h = (t1 - t0) / steps
    y = y0; t = t0
    do i = 1, steps
      k1 = rhs(t, y)
      k2 = rhs(t + h / 2d0, y + h * k1 / 2d0)
      y = y + h * k2
      t = t + h
    end do
    midpoint_method = y
  end function midpoint_method
end module midpoint_mod

program test_midpoint
  use midpoint_mod
  implicit none
  print *, "[Fortran Midpoint] y(1) =", midpoint_method(1d0, 0d0, 1d0, 1000)
  if (abs(midpoint_method(1d0, 0d0, 1d0, 1000) - exp(1d0)) > 1d-4) error stop "midpoint failed"
  print *, "[Fortran Midpoint] Test completed."
end program test_midpoint
