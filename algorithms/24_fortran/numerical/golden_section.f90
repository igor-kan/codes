module golden_mod
  implicit none
contains
  real(8) function f(x)
    real(8), intent(in) :: x
    f = (x - 3d0) * (x - 3d0)
  end function f

  real(8) function golden(a0, b0)
    real(8), intent(in) :: a0, b0
    real(8) :: a, b, c, d, fc, fd, invphi
    invphi = (sqrt(5d0) - 1d0) / 2d0
    a = a0
    b = b0
    c = b - invphi * (b - a)
    d = a + invphi * (b - a)
    fc = f(c)
    fd = f(d)
    do while (b - a > 1d-9)
      if (fc < fd) then
        b = d; d = c; fd = fc
        c = b - invphi * (b - a); fc = f(c)
      else
        a = c; c = d; fc = fd
        d = a + invphi * (b - a); fd = f(d)
      end if
    end do
    golden = (a + b) / 2d0
  end function golden
end module golden_mod

program test_golden
  use golden_mod
  implicit none
  real(8) :: x
  x = golden(-10d0, 10d0)
  print *, "[Fortran Golden Section] argmin =", x
  if (abs(x - 3d0) > 1d-6) error stop "golden section failed"
  print *, "[Fortran Golden Section] Test completed."
end program test_golden
