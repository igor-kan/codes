module aitken_mod
  implicit none
contains
  real(8) function aitken(x0, x1, x2)
    real(8), intent(in) :: x0, x1, x2
    real(8) :: denominator
    denominator = x2 - 2d0 * x1 + x0
    if (abs(denominator) < 1d-15) then
      aitken = x2
    else
      aitken = x2 - (x2 - x1) ** 2 / denominator
    end if
  end function aitken
end module aitken_mod

program test_aitken
  use aitken_mod
  implicit none
  real(8) :: sequence(3), n
  integer :: i
  if (abs(aitken(1d0, 0.5d0, 0.25d0)) > 1d-12) error stop "aitken geometric failed"
  do i = 1, 3
    n = dble(i - 1)
    sequence(i) = 2d0 - 2d0 * 0.5d0 ** n
  end do
  print *, "[Fortran Aitken] accelerated =", aitken(sequence(1), sequence(2), sequence(3))
  if (abs(aitken(sequence(1), sequence(2), sequence(3)) - 2d0) > 1d-12) error stop "aitken failed"
  print *, "[Fortran Aitken] Test completed."
end program test_aitken
