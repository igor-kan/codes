module steffensen_mod
  implicit none
contains
  real(8) function g(x)
    real(8), intent(in) :: x
    g = 0.5d0 * (x + 2d0 / x)
  end function g

  real(8) function steffensen(x0)
    real(8), intent(in) :: x0
    real(8) :: x, x1, x2, denominator, nxt
    integer :: i
    x = x0
    do i = 1, 100
      x1 = g(x)
      x2 = g(x1)
      denominator = x2 - 2d0 * x1 + x
      if (abs(denominator) < 1d-15) then
        steffensen = x2
        return
      end if
      nxt = x - (x1 - x) ** 2 / denominator
      if (abs(nxt - x) < 1d-12) then
        steffensen = nxt
        return
      end if
      x = nxt
    end do
    steffensen = x
  end function steffensen
end module steffensen_mod

program test_steffensen
  use steffensen_mod
  implicit none
  print *, "[Fortran Steffensen] root =", steffensen(1d0)
  if (abs(steffensen(1d0) - sqrt(2d0)) > 1d-12) error stop "steffensen failed"
  print *, "[Fortran Steffensen] Test completed."
end program test_steffensen
