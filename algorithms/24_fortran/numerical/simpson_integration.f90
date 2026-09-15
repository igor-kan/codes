module simpson_mod
  implicit none
contains
  real(8) function square(x)
    real(8), intent(in) :: x
    square = x * x
  end function square

  real(8) function simpson(a, b, n)
    real(8), intent(in) :: a, b
    integer, intent(in) :: n
    real(8) :: h, total
    integer :: i, steps
    steps = n
    if (mod(steps, 2) /= 0) steps = steps + 1
    h = (b - a) / steps
    total = square(a) + square(b)
    do i = 1, steps - 1
      if (mod(i, 2) == 1) then
        total = total + 4d0 * square(a + i * h)
      else
        total = total + 2d0 * square(a + i * h)
      end if
    end do
    simpson = total * h / 3d0
  end function simpson
end module simpson_mod

program test_simpson
  use simpson_mod
  implicit none
  real(8) :: value
  value = simpson(0d0, 1d0, 1000)
  print *, "[Fortran Simpson] integral =", value
  if (abs(value - 1d0 / 3d0) > 1d-12) error stop "simpson failed"
  print *, "[Fortran Simpson] Test completed."
end program test_simpson
