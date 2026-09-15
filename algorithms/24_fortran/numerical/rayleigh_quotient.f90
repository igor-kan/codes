module rayleigh_mod
  implicit none
contains
  subroutine rayleigh_quotient(matrix, vector, eigenvalue, x)
    real(8), intent(in) :: matrix(2, 2), vector(2)
    real(8), intent(out) :: eigenvalue, x(2)
    real(8) :: scale, p0, p1, norm, next_value, numerator, denominator
    integer :: iteration
    scale = max(abs(vector(1)), abs(vector(2)))
    x(1) = vector(1) / scale
    x(2) = vector(2) / scale
    eigenvalue = 0d0
    do iteration = 1, 100
      p0 = matrix(1, 1) * x(1) + matrix(1, 2) * x(2)
      p1 = matrix(2, 1) * x(1) + matrix(2, 2) * x(2)
      norm = max(abs(p0), abs(p1))
      x(1) = p0 / norm
      x(2) = p1 / norm
      numerator = x(1) * (matrix(1, 1) * x(1) + matrix(1, 2) * x(2)) + &
                  x(2) * (matrix(2, 1) * x(1) + matrix(2, 2) * x(2))
      denominator = x(1) * x(1) + x(2) * x(2)
      next_value = numerator / denominator
      if (abs(next_value - eigenvalue) < 1d-12) then
        eigenvalue = next_value
        return
      end if
      eigenvalue = next_value
    end do
  end subroutine rayleigh_quotient
end module rayleigh_mod

program test_rayleigh
  use rayleigh_mod
  implicit none
  real(8) :: matrix(2, 2), vector(2), eigenvalue, x(2)
  matrix(1, 1) = 2; matrix(1, 2) = 1
  matrix(2, 1) = 1; matrix(2, 2) = 2
  vector = (/1d0, 0d0/)
  call rayleigh_quotient(matrix, vector, eigenvalue, x)
  print *, "[Fortran Rayleigh] eigenvalue =", eigenvalue
  if (abs(eigenvalue - 3d0) > 1d-9) error stop "rayleigh failed"
  print *, "[Fortran Rayleigh] Test completed."
end program test_rayleigh
