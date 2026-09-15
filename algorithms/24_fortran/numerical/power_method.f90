module power_mod
  implicit none
contains
  subroutine power_method(matrix, n, eigenvalue, vector)
    integer, intent(in) :: n
    real(8), intent(in) :: matrix(n, n)
    real(8), intent(out) :: eigenvalue, vector(n)
    real(8) :: product(n), norm
    integer :: i, j, iteration
    do i = 1, n
      vector(i) = 1d0
    end do
    eigenvalue = 0d0
    do iteration = 1, 1000
      do i = 1, n
        product(i) = 0d0
        do j = 1, n
          product(i) = product(i) + matrix(i, j) * vector(j)
        end do
      end do
      norm = 0d0
      do i = 1, n
        norm = max(norm, abs(product(i)))
      end do
      do i = 1, n
        vector(i) = product(i) / norm
      end do
      if (abs(norm - eigenvalue) < 1d-12) then
        eigenvalue = norm
        exit
      end if
      eigenvalue = norm
    end do
  end subroutine power_method
end module power_mod

program test_power
  use power_mod
  implicit none
  real(8) :: matrix(2, 2), eigenvalue, vector(2)
  matrix(1, 1) = 4; matrix(1, 2) = 1
  matrix(2, 1) = 2; matrix(2, 2) = 3
  call power_method(matrix, 2, eigenvalue, vector)
  print *, "[Fortran Power Method] eigenvalue =", eigenvalue
  if (abs(eigenvalue - 5d0) > 1d-9) error stop "power method failed"
  print *, "[Fortran Power Method] Test completed."
end program test_power
