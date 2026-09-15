module fixed_mod
  implicit none
contains
  real(8) function g(x)
    real(8), intent(in) :: x
    g = 0.5d0 * (x + 2d0 / x)
  end function g

  real(8) function fixed_point(x0)
    real(8), intent(in) :: x0
    real(8) :: x, nxt
    integer :: i
    x = x0
    do i = 1, 200
      nxt = g(x)
      if (abs(nxt - x) < 1d-12) then
        fixed_point = nxt
        return
      end if
      x = nxt
    end do
    fixed_point = x
  end function fixed_point
end module fixed_mod

program test_fixed
  use fixed_mod
  implicit none
  print *, "[Fortran Fixed Point] root =", fixed_point(1d0)
  if (abs(fixed_point(1d0) - sqrt(2d0)) > 1d-9) error stop "fixed point failed"
  print *, "[Fortran Fixed Point] Test completed."
end program test_fixed
