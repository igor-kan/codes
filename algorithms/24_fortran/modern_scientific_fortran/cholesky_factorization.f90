! Modern Fortran 2018 Cholesky Factorization L L^T
module cholesky_factorization_mod
    use, intrinsic :: iso_fortran_env, only: real64, int32
    implicit none
    private
    public :: cholesky_decompose, cholesky_solve

contains

    subroutine cholesky_decompose(A, L, n, info)
        integer(int32), intent(in) :: n
        real(real64), dimension(n, n), intent(in) :: A
        real(real64), dimension(n, n), intent(out) :: L
        integer(int32), intent(out) :: info

        integer(int32) :: i, j, k
        real(real64) :: s

        info = 0
        L = 0.0_real64

        do i = 1, n
            do j = 1, i
                s = 0.0_real64
                do k = 1, j - 1
                    s = s + L(i, k) * L(j, k)
                end do
                if (i == j) then
                    s = A(i, i) - s
                    if (s <= 0.0_real64) then
                        info = i
                        return
                    end if
                    L(i, i) = sqrt(s)
                else
                    L(i, j) = (A(i, j) - s) / L(j, j)
                end if
            end do
        end do
    end subroutine cholesky_decompose

    subroutine cholesky_solve(L, b, x, n)
        integer(int32), intent(in) :: n
        real(real64), dimension(n, n), intent(in) :: L
        real(real64), dimension(n), intent(in) :: b
        real(real64), dimension(n), intent(out) :: x

        real(real64), dimension(n) :: y
        integer(int32) :: i, j

        ! Forward solve L y = b
        do i = 1, n
            y(i) = b(i)
            do j = 1, i - 1
                y(i) = y(i) - L(i, j) * y(j)
            end do
            y(i) = y(i) / L(i, i)
        end do

        ! Backward solve L^T x = y
        do i = n, 1, -1
            x(i) = y(i)
            do j = i + 1, n
                x(i) = x(i) - L(j, i) * x(j)
            end do
            x(i) = x(i) / L(i, i)
        end do
    end subroutine cholesky_solve

end module cholesky_factorization_mod
