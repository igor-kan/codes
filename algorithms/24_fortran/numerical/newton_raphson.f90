module newton_mod
  implicit none
contains
  real(8) function f(x)
    real(8), intent(in) :: x
    f = x * x - 2d0
  end function f

  real(8) function df(x)
    real(8), intent(in) :: x
    df = 2d0 * x
  end function df

  real(8) function newton(x0)
    real(8), intent(in) :: x0
    real(8) :: x
    integer :: i
    x = x0
    do i = 1, 100
      if (abs(f(x)) < 1d-12) exit
      x = x - f(x) / df(x)
    end do
    newton = x
  end function newton
end module newton_mod

program test_newton
  use newton_mod
  implicit none
  real(8) :: root
  root = newton(1d0)
  print *, "[Fortran Newton-Raphson] root =", root
  if (abs(root - sqrt(2d0)) > 1d-9) error stop "newton failed"
  print *, "[Fortran Newton-Raphson] Test completed."
end program test_newton
