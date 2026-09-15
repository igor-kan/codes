module linear_interp_mod
  implicit none
contains
  real(8) function linear_interpolation(xs, ys, n, x)
    integer, intent(in) :: n
    real(8), intent(in) :: xs(n), ys(n), x
    real(8) :: slope
    integer :: i
    if (x <= xs(1)) then
      linear_interpolation = ys(1)
      return
    end if
    if (x >= xs(n)) then
      linear_interpolation = ys(n)
      return
    end if
    do i = 2, n
      if (x <= xs(i)) then
        slope = (ys(i) - ys(i - 1)) / (xs(i) - xs(i - 1))
        linear_interpolation = ys(i - 1) + slope * (x - xs(i - 1))
        return
      end if
    end do
    linear_interpolation = ys(n)
  end function linear_interpolation
end module linear_interp_mod

program test_linear
  use linear_interp_mod
  implicit none
  real(8) :: xs(3) = (/0d0, 1d0, 2d0/), ys(3) = (/0d0, 2d0, 4d0/)
  print *, "[Fortran Linear Interpolation] value =", linear_interpolation(xs, ys, 3, 0.5d0)
  if (abs(linear_interpolation(xs, ys, 3, 0.5d0) - 1d0) > 1d-12) error stop "linear failed"
  print *, "[Fortran Linear Interpolation] Test completed."
end program test_linear
