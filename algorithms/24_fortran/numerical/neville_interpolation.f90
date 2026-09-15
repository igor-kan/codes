module neville_mod
  implicit none
contains
  real(8) function neville_interpolation(xs, ys, n, x)
    integer, intent(in) :: n
    real(8), intent(in) :: xs(n), ys(n), x
    real(8) :: table(16)
    integer :: i, k
    do i = 1, n
      table(i) = ys(i)
    end do
    do k = 1, n - 1
      do i = 1, n - k
        table(i) = ((x - xs(i + k)) * table(i) + (xs(i) - x) * table(i + 1)) / (xs(i) - xs(i + k))
      end do
    end do
    neville_interpolation = table(1)
  end function neville_interpolation
end module neville_mod

program test_neville
  use neville_mod
  implicit none
  real(8) :: xs(3) = (/0d0, 1d0, 2d0/), ys(3) = (/1d0, 3d0, 2d0/)
  print *, "[Fortran Neville] P(1.5) =", neville_interpolation(xs, ys, 3, 1.5d0)
  if (abs(neville_interpolation(xs, ys, 3, 1.5d0) - 2.875d0) > 1d-12) error stop "neville failed"
  print *, "[Fortran Neville] Test completed."
end program test_neville
