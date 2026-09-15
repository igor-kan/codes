module lagrange_mod
  implicit none
contains
  real(8) function interpolate(xs, ys, x, n)
    integer, intent(in) :: n
    real(8), intent(in) :: xs(n), ys(n), x
    real(8) :: term
    integer :: i, j
    interpolate = 0d0
    do i = 1, n
      term = ys(i)
      do j = 1, n
        if (i /= j) term = term * (x - xs(j)) / (xs(i) - xs(j))
      end do
      interpolate = interpolate + term
    end do
  end function interpolate
end module lagrange_mod

program test_lagrange
  use lagrange_mod
  implicit none
  real(8) :: xs(3), ys(3), value
  xs = (/0d0, 1d0, 2d0/)
  ys = (/1d0, 3d0, 2d0/)
  value = interpolate(xs, ys, 1.5d0, 3)
  print *, "[Fortran Lagrange] P(1.5) =", value
  if (abs(value - 2.875d0) > 1d-9) error stop "lagrange failed"
  print *, "[Fortran Lagrange] Test completed."
end program test_lagrange
