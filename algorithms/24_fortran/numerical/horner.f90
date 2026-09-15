module horner_mod
  implicit none
contains
  subroutine horner_with_derivative(c, n, x, value, derivative)
    integer, intent(in) :: n
    real(8), intent(in) :: c(n), x
    real(8), intent(out) :: value, derivative
    integer :: i
    value = 0d0
    derivative = 0d0
    do i = n, 1, -1
      derivative = derivative * x + value
      value = value * x + c(i)
    end do
  end subroutine horner_with_derivative
end module horner_mod

program test_horner
  use horner_mod
  implicit none
  real(8) :: c(4) = (/-1d0, 2d0, -6d0, 2d0/), value, derivative
  call horner_with_derivative(c, 4, 3d0, value, derivative)
  print *, "[Fortran Horner] P(3) =", value, "P'(3) =", derivative
  if (abs(value - 5d0) > 1d-9 .or. abs(derivative - 20d0) > 1d-9) error stop "horner failed"
  print *, "[Fortran Horner] Test completed."
end program test_horner
