! Modern Fortran 2018 Thomas Tridiagonal Linear System Solver O(N)
module thomas_tridiagonal_mod
    use, intrinsic :: iso_fortran_env, only: real64, int32
    implicit none
    private
    public :: solve_tridiagonal

contains

    subroutine solve_tridiagonal(a, b, c, d, x, n, status)
        integer(int32), intent(in) :: n
        real(real64), dimension(n), intent(in) :: a, b, c, d
        real(real64), dimension(n), intent(out) :: x
        integer(int32), intent(out) :: status
        
        real(real64), dimension(n) :: c_prime, d_prime
        real(real64) :: denom
        integer(int32) :: i

        status = 0
        if (abs(b(1)) < 1.0e-15_real64) then
            status = 1
            return
        end if

        c_prime(1) = c(1) / b(1)
        d_prime(1) = d(1) / b(1)

        do i = 2, n
            denom = b(i) - a(i) * c_prime(i - 1)
            if (abs(denom) < 1.0e-15_real64) then
                status = i
                return
            end if
            if (i < n) then
                c_prime(i) = c(i) / denom
            end if
            d_prime(i) = (d(i) - a(i) * d_prime(i - 1)) / denom
        end do

        x(n) = d_prime(n)
        do i = n - 1, 1, -1
            x(i) = d_prime(i) - c_prime(i) * x(i + 1)
        end do
    end subroutine solve_tridiagonal

end module thomas_tridiagonal_mod
