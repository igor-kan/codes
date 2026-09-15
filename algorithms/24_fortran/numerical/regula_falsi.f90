module regula_mod
  implicit none
contains
  real(8) function f(x)
    real(8), intent(in) :: x
    f = x * x - 2d0
  end function f

  real(8) function regula_falsi(a, b)
    real(8), intent(in) :: a, b
    real(8) :: lo, hi, fa, fb, c, fc
    integer :: i
    lo = a; hi = b
    fa = f(lo); fb = f(hi)
    c = lo
    do i = 1, 200
      c = (lo * fb - hi * fa) / (fb - fa)
      fc = f(c)
      if (abs(fc) < 1d-12) then
        regula_falsi = c
        return
      end if
      if (fa * fc < 0d0) then
        hi = c; fb = fc
      else
        lo = c; fa = fc
      end if
    end do
    regula_falsi = c
  end function regula_falsi
end module regula_mod

program test_regula
  use regula_mod
  implicit none
  print *, "[Fortran Regula Falsi] root =", regula_falsi(0d0, 2d0)
  if (abs(regula_falsi(0d0, 2d0) - sqrt(2d0)) > 1d-9) error stop "regula falsi failed"
  print *, "[Fortran Regula Falsi] Test completed."
end program test_regula
