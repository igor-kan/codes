module boole_mod
  implicit none
contains
  real(8) function square(x)
    real(8), intent(in) :: x
    square = x * x
  end function square

  real(8) function boole_rule(a, b, n)
    real(8), intent(in) :: a, b
    integer, intent(in) :: n
    integer :: steps, i
    real(8) :: h, total
    steps = n
    if (mod(steps, 4) /= 0) steps = steps + 4 - mod(steps, 4)
    h = (b - a) / steps
    total = 7d0 * (square(a) + square(b))
    do i = 1, steps - 1
      if (mod(i, 4) == 0) then
        total = total + 14d0 * square(a + i * h)
      else if (mod(i, 2) == 0) then
        total = total + 12d0 * square(a + i * h)
      else
        total = total + 32d0 * square(a + i * h)
      end if
    end do
    boole_rule = 2d0 * h / 45d0 * total
  end function boole_rule
end module boole_mod

program test_boole
  use boole_mod
  implicit none
  real(8) :: value
  value = boole_rule(0d0, 1d0, 998)
  print *, "[Fortran Boole Rule] integral =", value
  if (abs(value - 1d0 / 3d0) > 1d-12) error stop "boole failed"
  print *, "[Fortran Boole Rule] Test completed."
end program test_boole
