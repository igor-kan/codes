module least_squares_mod
  implicit none
contains
  subroutine least_squares_linear(xs, ys, n, intercept, slope)
    integer, intent(in) :: n
    real(8), intent(in) :: xs(n), ys(n)
    real(8), intent(out) :: intercept, slope
    real(8) :: mean_x, mean_y, numerator, denominator
    integer :: i
    mean_x = 0d0; mean_y = 0d0
    do i = 1, n
      mean_x = mean_x + xs(i) / n
      mean_y = mean_y + ys(i) / n
    end do
    numerator = 0d0; denominator = 0d0
    do i = 1, n
      numerator = numerator + (xs(i) - mean_x) * (ys(i) - mean_y)
      denominator = denominator + (xs(i) - mean_x) ** 2
    end do
    slope = numerator / denominator
    intercept = mean_y - slope * mean_x
  end subroutine least_squares_linear
end module least_squares_mod

program test_least_squares
  use least_squares_mod
  implicit none
  real(8) :: xs(4) = (/0d0, 1d0, 2d0, 3d0/), ys(4) = (/1d0, 3d0, 5d0, 7d0/)
  real(8) :: intercept, slope
  call least_squares_linear(xs, ys, 4, intercept, slope)
  print *, "[Fortran Least Squares] intercept =", intercept, " slope =", slope
  if (abs(intercept - 1d0) > 1d-12 .or. abs(slope - 2d0) > 1d-12) error stop "least squares failed"
  print *, "[Fortran Least Squares] Test completed."
end program test_least_squares
