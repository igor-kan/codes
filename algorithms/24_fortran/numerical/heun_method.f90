module heun_mod
  implicit none
contains
  real(8) function rhs(t, y)
    real(8), intent(in) :: t, y
    rhs = y
  end function rhs

  real(8) function heun_method(y0, t0, t1, steps)
    real(8), intent(in) :: y0, t0, t1
    integer, intent(in) :: steps
    real(8) :: h, y, t, k1, k2
    integer :: i
    h = (t1 - t0) / steps
    y = y0; t = t0
    do i = 1, steps
      k1 = rhs(t, y)
      k2 = rhs(t + h, y + h * k1)
      y = y + 0.5d0 * h * (k1 + k2)
      t = t + h
    end do
    heun_method = y
  end function heun_method
end module heun_mod

program test_heun
  use heun_mod
  implicit none
  print *, "[Fortran Heun] y(1) =", heun_method(1d0, 0d0, 1d0, 1000)
  if (abs(heun_method(1d0, 0d0, 1d0, 1000) - exp(1d0)) > 1d-4) error stop "heun failed"
  print *, "[Fortran Heun] Test completed."
end program test_heun
