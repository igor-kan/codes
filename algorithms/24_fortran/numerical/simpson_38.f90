module simpson38_mod
  implicit none
contains
  real(8) function square(x)
    real(8), intent(in) :: x
    square = x * x
  end function square

  real(8) function simpson_38(a, b, n)
    real(8), intent(in) :: a, b
    integer, intent(in) :: n
    integer :: steps, i
    real(8) :: h, total
    steps = n
    if (mod(steps, 3) /= 0) steps = steps + 3 - mod(steps, 3)
    h = (b - a) / steps
    total = square(a) + square(b)
    do i = 1, steps - 1
      if (mod(i, 3) /= 0) then
        total = total + 3d0 * square(a + i * h)
      else
        total = total + 2d0 * square(a + i * h)
      end if
    end do
    simpson_38 = 3d0 * h / 8d0 * total
  end function simpson_38
end module simpson38_mod

program test_simpson38
  use simpson38_mod
  implicit none
  real(8) :: value
  value = simpson_38(0d0, 1d0, 999)
  print *, "[Fortran Simpson 3/8] integral =", value
  if (abs(value - 1d0 / 3d0) > 1d-12) error stop "simpson 3/8 failed"
  print *, "[Fortran Simpson 3/8] Test completed."
end program test_simpson38
