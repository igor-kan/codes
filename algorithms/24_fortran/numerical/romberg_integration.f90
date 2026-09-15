module romberg_mod
  implicit none
contains
  real(8) function square(x)
    real(8), intent(in) :: x
    square = x * x
  end function square

  real(8) function romberg(a, b, order)
    real(8), intent(in) :: a, b
    integer, intent(in) :: order
    real(8) :: r(0:order, 0:order), h, total
    integer :: i, k, m
    h = b - a
    r(0, 0) = 0.5d0 * h * (square(a) + square(b))
    do i = 1, order
      h = h / 2d0
      total = 0d0
      do k = 1, 2**(i - 1)
        total = total + square(a + (2 * k - 1) * h)
      end do
      r(i, 0) = 0.5d0 * r(i - 1, 0) + h * total
      do m = 1, i
        r(i, m) = r(i, m - 1) + (r(i, m - 1) - r(i - 1, m - 1)) / (4d0**m - 1d0)
      end do
    end do
    romberg = r(order, order)
  end function romberg
end module romberg_mod

program test_romberg
  use romberg_mod
  implicit none
  real(8) :: value
  value = romberg(0d0, 1d0, 6)
  print *, "[Fortran Romberg] integral =", value
  if (abs(value - 1d0 / 3d0) > 1d-12) error stop "romberg failed"
  print *, "[Fortran Romberg] Test completed."
end program test_romberg
