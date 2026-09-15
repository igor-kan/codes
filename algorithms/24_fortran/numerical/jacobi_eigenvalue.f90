module jacobi_mod
  implicit none
contains
  subroutine jacobi_eigenvalue(a, n, eigenvalues)
    integer, intent(in) :: n
    real(8), intent(inout) :: a(n, n)
    real(8), intent(out) :: eigenvalues(n)
    real(8) :: theta, c, s, largest, akp, akq, apk, aqk
    integer :: i, j, k, p, q, iteration
    do iteration = 1, 100
      p = 1
      q = 2
      largest = 0d0
      do i = 1, n
        do j = i + 1, n
          if (abs(a(i, j)) > largest) then
            largest = abs(a(i, j))
            p = i
            q = j
          end if
        end do
      end do
      if (largest < 1d-12) exit
      theta = 0.5d0 * atan2(2d0 * a(p, q), a(q, q) - a(p, p))
      c = cos(theta)
      s = sin(theta)
      do k = 1, n
        akp = a(k, p)
        akq = a(k, q)
        a(k, p) = c * akp - s * akq
        a(k, q) = s * akp + c * akq
      end do
      do k = 1, n
        apk = a(p, k)
        aqk = a(q, k)
        a(p, k) = c * apk - s * aqk
        a(q, k) = s * apk + c * aqk
      end do
    end do
    do i = 1, n
      eigenvalues(i) = a(i, i)
    end do
  end subroutine jacobi_eigenvalue
end module jacobi_mod

program test_jacobi
  use jacobi_mod
  implicit none
  real(8) :: a(3, 3), eigenvalues(3), total, product
  integer :: i
  a(1, 1) = 4; a(1, 2) = 1; a(1, 3) = 0
  a(2, 1) = 1; a(2, 2) = 3; a(2, 3) = 1
  a(3, 1) = 0; a(3, 2) = 1; a(3, 3) = 2
  call jacobi_eigenvalue(a, 3, eigenvalues)
  total = 0d0
  product = 1d0
  do i = 1, 3
    total = total + eigenvalues(i)
    product = product * eigenvalues(i)
  end do
  print *, "[Fortran Jacobi] eigenvalues =", eigenvalues
  if (abs(total - 9d0) > 1d-9 .or. abs(product - 18d0) > 1d-9) error stop "jacobi failed"
  print *, "[Fortran Jacobi] Test completed."
end program test_jacobi
