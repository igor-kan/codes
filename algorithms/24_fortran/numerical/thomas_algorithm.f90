module thomas_mod
  implicit none
contains
  subroutine thomas_algorithm(lower, diagonal, upper, rhs, n, x)
    integer, intent(in) :: n
    real(8), intent(in) :: lower(n), diagonal(n), upper(n), rhs(n)
    real(8), intent(out) :: x(n)
    real(8) :: c(16), d(16), denominator
    integer :: i
    c(1) = upper(1) / diagonal(1)
    d(1) = rhs(1) / diagonal(1)
    do i = 2, n
      denominator = diagonal(i) - lower(i) * c(i - 1)
      if (i < n) then
        c(i) = upper(i) / denominator
      else
        c(i) = 0d0
      end if
      d(i) = (rhs(i) - lower(i) * d(i - 1)) / denominator
    end do
    x(n) = d(n)
    do i = n - 1, 1, -1
      x(i) = d(i) - c(i) * x(i + 1)
    end do
  end subroutine thomas_algorithm
end module thomas_mod

program test_thomas
  use thomas_mod
  implicit none
  real(8) :: lower(3) = (/0d0, -1d0, -1d0/), diagonal(3) = (/2d0, 2d0, 2d0/)
  real(8) :: upper(3) = (/-1d0, -1d0, 0d0/), rhs(3) = (/1d0, 0d0, 1d0/), x(3)
  integer :: i
  call thomas_algorithm(lower, diagonal, upper, rhs, 3, x)
  print *, "[Fortran Thomas] x =", x
  do i = 1, 3
    if (abs(x(i) - 1d0) > 1d-12) error stop "thomas failed"
  end do
  print *, "[Fortran Thomas] Test completed."
end program test_thomas
