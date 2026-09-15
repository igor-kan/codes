module qr_mod
  implicit none
contains
  subroutine qr_decomposition(matrix, n, q, r)
    integer, intent(in) :: n
    real(8), intent(in) :: matrix(n, n)
    real(8), intent(out) :: q(n, n), r(n, n)
    real(8) :: v(n)
    integer :: i, j, k
    q = 0d0
    r = 0d0
    do j = 1, n
      do i = 1, n
        v(i) = matrix(i, j)
      end do
      do i = 1, j - 1
        r(i, j) = 0d0
        do k = 1, n
          r(i, j) = r(i, j) + q(k, i) * v(k)
        end do
        do k = 1, n
          v(k) = v(k) - r(i, j) * q(k, i)
        end do
      end do
      r(j, j) = 0d0
      do k = 1, n
        r(j, j) = r(j, j) + v(k) * v(k)
      end do
      r(j, j) = sqrt(r(j, j))
      do k = 1, n
        q(k, j) = v(k) / r(j, j)
      end do
    end do
  end subroutine qr_decomposition
end module qr_mod

program test_qr
  use qr_mod
  implicit none
  real(8) :: matrix(2, 2), q(2, 2), r(2, 2), next(2, 2), lo, hi
  integer :: i, j, k, iteration
  matrix(1, 1) = 2; matrix(1, 2) = 1
  matrix(2, 1) = 1; matrix(2, 2) = 2
  do iteration = 1, 1000
    call qr_decomposition(matrix, 2, q, r)
    do i = 1, 2
      do j = 1, 2
        next(i, j) = 0d0
        do k = 1, 2
          next(i, j) = next(i, j) + r(i, k) * q(k, j)
        end do
      end do
    end do
    matrix = next
  end do
  print *, "[Fortran QR Algorithm] diagonal =", matrix(1, 1), matrix(2, 2)
  lo = min(matrix(1, 1), matrix(2, 2))
  hi = max(matrix(1, 1), matrix(2, 2))
  if (abs(lo - 1d0) > 1d-6 .or. abs(hi - 3d0) > 1d-6) error stop "qr failed"
  print *, "[Fortran QR Algorithm] Test completed."
end program test_qr
