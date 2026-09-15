module lu_mod
  implicit none
contains
  subroutine lu_solve(a, b, x, n)
    integer, intent(in) :: n
    real(8), intent(inout) :: a(n, n), b(n)
    real(8), intent(out) :: x(n)
    integer :: col, r, k, piv
    real(8) :: f, s, tmp
    do col = 1, n
      piv = col
      do r = col + 1, n
        if (abs(a(r, col)) > abs(a(piv, col))) piv = r
      end do
      if (piv /= col) then
        do k = 1, n
          tmp = a(col, k); a(col, k) = a(piv, k); a(piv, k) = tmp
        end do
        tmp = b(col); b(col) = b(piv); b(piv) = tmp
      end if
      do r = col + 1, n
        f = a(r, col) / a(col, col)
        do k = col, n
          a(r, k) = a(r, k) - f * a(col, k)
        end do
        b(r) = b(r) - f * b(col)
      end do
    end do
    do r = n, 1, -1
      s = b(r)
      do k = r + 1, n
        s = s - a(r, k) * x(k)
      end do
      x(r) = s / a(r, r)
    end do
  end subroutine lu_solve
end module lu_mod

program test_lu
  use lu_mod
  implicit none
  real(8) :: a(3, 3), b(3), x(3)
  a(1, 1) = 2;  a(1, 2) = 1;  a(1, 3) = -1
  a(2, 1) = -3; a(2, 2) = -1; a(2, 3) = 2
  a(3, 1) = -2; a(3, 2) = 1;  a(3, 3) = 2
  b = (/8d0, -11d0, -3d0/)
  call lu_solve(a, b, x, 3)
  print *, "[Fortran LU] x =", x
  if (abs(x(1) - 2d0) > 1d-9 .or. abs(x(2) - 3d0) > 1d-9 .or. abs(x(3) + 1d0) > 1d-9) then
    error stop "lu decomposition failed"
  end if
  print *, "[Fortran LU] Test completed."
end program test_lu
