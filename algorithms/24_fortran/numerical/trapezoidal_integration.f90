module trapezoid_mod
  implicit none
contains
  real(8) function square(x)
    real(8), intent(in) :: x
    square = x * x
  end function square

  real(8) function trapezoid(a, b, n)
    real(8), intent(in) :: a, b
    integer, intent(in) :: n
    real(8) :: h, total
    integer :: i
    h = (b - a) / n
    total = 0.5d0 * (square(a) + square(b))
    do i = 1, n - 1
      total = total + square(a + i * h)
    end do
    trapezoid = total * h
  end function trapezoid
end module trapezoid_mod

program test_trapezoid
  use trapezoid_mod
  implicit none
  real(8) :: value
  value = trapezoid(0d0, 1d0, 100000)
  print *, "[Fortran Trapezoidal] integral =", value
  if (abs(value - 1d0 / 3d0) > 1d-8) error stop "trapezoidal failed"
  print *, "[Fortran Trapezoidal] Test completed."
end program test_trapezoid
