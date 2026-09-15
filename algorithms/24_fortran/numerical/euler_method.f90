module euler_mod
  implicit none
contains
  real(8) function rhs(t, y)
    real(8), intent(in) :: t, y
    rhs = y
  end function rhs

  real(8) function euler_method(y0, t0, t1, steps)
    real(8), intent(in) :: y0, t0, t1
    integer, intent(in) :: steps
    real(8) :: h, y, t
    integer :: i
    h = (t1 - t0) / steps
    y = y0; t = t0
    do i = 1, steps
      y = y + h * rhs(t, y)
      t = t + h
    end do
    euler_method = y
  end function euler_method
end module euler_mod

program test_euler
  use euler_mod
  implicit none
  print *, "[Fortran Euler] y(1) =", euler_method(1d0, 0d0, 1d0, 1000)
  if (abs(euler_method(1d0, 0d0, 1d0, 1000) - exp(1d0)) > 1d-2) error stop "euler failed"
  print *, "[Fortran Euler] Test completed."
end program test_euler
