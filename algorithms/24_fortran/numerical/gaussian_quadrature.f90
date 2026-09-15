module gauss_mod
  implicit none
contains
  real(8) function square(x)
    real(8), intent(in) :: x
    square = x * x
  end function square

  real(8) function seventh(x)
    real(8), intent(in) :: x
    seventh = x**7
  end function seventh

  real(8) function gaussian_quadrature(func, a, b)
    interface
      real(8) function func(x)
        real(8), intent(in) :: x
      end function func
    end interface
    real(8), intent(in) :: a, b
    real(8) :: nodes(5), weights(5), midpoint, half, total
    integer :: i
    nodes = (/0d0, -0.5384693101056831d0, 0.5384693101056831d0, -0.9061798459386640d0, 0.9061798459386640d0/)
    weights = (/0.5688888888888889d0, 0.4786286704993665d0, 0.4786286704993665d0, &
                0.2369268850561891d0, 0.2369268850561891d0/)
    midpoint = 0.5d0 * (a + b)
    half = 0.5d0 * (b - a)
    total = 0d0
    do i = 1, 5
      total = total + weights(i) * func(midpoint + half * nodes(i))
    end do
    gaussian_quadrature = total * half
  end function gaussian_quadrature
end module gauss_mod

program test_gauss
  use gauss_mod
  implicit none
  print *, "[Fortran Gaussian Quadrature] x^2 =", gaussian_quadrature(square, 0d0, 1d0)
  if (abs(gaussian_quadrature(square, 0d0, 1d0) - 1d0 / 3d0) > 1d-12) error stop "gauss failed"
  if (abs(gaussian_quadrature(seventh, 0d0, 1d0) - 1d0 / 8d0) > 1d-12) error stop "gauss degree failed"
  print *, "[Fortran Gaussian Quadrature] Test completed."
end program test_gauss
