module bisection_mod
  implicit none
contains
  real(8) function f(x)
    real(8), intent(in) :: x
    f = x * x - 2d0
  end function f

  real(8) function bisection(a, b)
    real(8), intent(in) :: a, b
    real(8) :: lo, hi, fa, c, fc
    integer :: i
    lo = a; hi = b
    fa = f(lo)
    do i = 1, 200
      c = 0.5d0 * (lo + hi)
      fc = f(c)
      if (fc == 0d0 .or. (hi - lo) / 2d0 < 1d-12) then
        bisection = c
        return
      end if
      if (fa * fc < 0d0) then
        hi = c
      else
        lo = c; fa = fc
      end if
    end do
    bisection = 0.5d0 * (lo + hi)
  end function bisection
end module bisection_mod

program test_bisection
  use bisection_mod
  implicit none
  print *, "[Fortran Bisection] root =", bisection(0d0, 2d0)
  if (abs(bisection(0d0, 2d0) - sqrt(2d0)) > 1d-9) error stop "bisection failed"
  print *, "[Fortran Bisection] Test completed."
end program test_bisection
