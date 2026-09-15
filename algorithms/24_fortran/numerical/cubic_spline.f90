module spline_mod
  implicit none
contains
  subroutine natural_cubic_spline(xs, ys, n, b, c, d)
    integer, intent(in) :: n
    real(8), intent(in) :: xs(n), ys(n)
    real(8), intent(out) :: b(n - 1), c(n), d(n - 1)
    real(8) :: h(n - 1), alpha(n), l(n), mu(n), z(n)
    integer :: i, j
    do i = 1, n - 1
      h(i) = xs(i + 1) - xs(i)
    end do
    alpha = 0d0
    do i = 2, n - 1
      alpha(i) = 3d0 / h(i) * (ys(i + 1) - ys(i)) - 3d0 / h(i - 1) * (ys(i) - ys(i - 1))
    end do
    l = 0d0; mu = 0d0; z = 0d0
    l(1) = 1d0
    do i = 2, n - 1
      l(i) = 2d0 * (xs(i + 1) - xs(i - 1)) - h(i - 1) * mu(i - 1)
      mu(i) = h(i) / l(i)
      z(i) = (alpha(i) - h(i - 1) * z(i - 1)) / l(i)
    end do
    b = 0d0; c = 0d0; d = 0d0
    do j = n - 1, 1, -1
      c(j) = z(j) - mu(j) * c(j + 1)
      b(j) = (ys(j + 1) - ys(j)) / h(j) - h(j) * (c(j + 1) + 2d0 * c(j)) / 3d0
      d(j) = (c(j + 1) - c(j)) / (3d0 * h(j))
    end do
  end subroutine natural_cubic_spline

  real(8) function spline_evaluate(xs, ys, b, c, d, n, x)
    integer, intent(in) :: n
    real(8), intent(in) :: xs(n), ys(n), b(n - 1), c(n), d(n - 1), x
    integer :: segment, i
    real(8) :: dx
    segment = n - 1
    do i = 1, n - 1
      if (xs(i) <= x .and. x <= xs(i + 1)) then
        segment = i
        exit
      end if
    end do
    dx = x - xs(segment)
    spline_evaluate = ys(segment) + b(segment) * dx + c(segment) * dx**2 + d(segment) * dx**3
  end function spline_evaluate
end module spline_mod

program test_spline
  use spline_mod
  implicit none
  real(8) :: xs(4) = (/0d0, 1d0, 2d0, 3d0/)
  real(8) :: ys(4) = (/0d0, 1d0, 0d0, 1d0/)
  real(8) :: b(3), c(4), d(3), value
  integer :: i
  call natural_cubic_spline(xs, ys, 4, b, c, d)
  do i = 1, 4
    value = spline_evaluate(xs, ys, b, c, d, 4, xs(i))
    if (abs(value - ys(i)) > 1d-9) error stop "cubic spline failed"
  end do
  print *, "[Fortran Cubic Spline] interpolation verified"
end program test_spline
