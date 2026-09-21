! Modern Fortran 2018 LU Decomposition with Partial Pivoting
module lu_decomposition_mod
    use, intrinsic :: iso_fortran_env, only: real64, int32
    implicit none
    private
    public :: lu_factor, lu_solve

contains

    subroutine lu_factor(A, piv, n, info)
        integer(int32), intent(in) :: n
        real(real64), dimension(n, n), intent(inout) :: A
        integer(int32), dimension(n), intent(out) :: piv
        integer(int32), intent(out) :: info

        integer(int32) :: i, j, k, max_idx
        real(real64) :: max_val, tmp

        info = 0
        do i = 1, n
            piv(i) = i
        end do

        do k = 1, n - 1
            max_idx = k
            max_val = abs(A(k, k))
            do i = k + 1, n
                if (abs(A(i, k)) > max_val) then
                    max_val = abs(A(i, k))
                    max_idx = i
                end if
            end do

            if (max_val < 1.0e-15_real64) then
                info = k
                return
            end if

            if (max_idx /= k) then
                j = piv(k)
                piv(k) = piv(max_idx)
                piv(max_idx) = j
                do j = 1, n
                    tmp = A(k, j)
                    A(k, j) = A(max_idx, j)
                    A(max_idx, j) = tmp
                end do
            end if

            do i = k + 1, n
                A(i, k) = A(i, k) / A(k, k)
                do j = k + 1, n
                    A(i, j) = A(i, j) - A(i, k) * A(k, j)
                end do
            end do
        end do
    end subroutine lu_factor

    subroutine lu_solve(A, piv, b, x, n)
        integer(int32), intent(in) :: n
        real(real64), dimension(n, n), intent(in) :: A
        integer(int32), dimension(n), intent(in) :: piv
        real(real64), dimension(n), intent(in) :: b
        real(real64), dimension(n), intent(out) :: x

        real(real64), dimension(n) :: y
        integer(int32) :: i, j

        ! Forward substitution with pivoting L y = P b
        do i = 1, n
            y(i) = b(piv(i))
            do j = 1, i - 1
                y(i) = y(i) - A(i, j) * y(j)
            end do
        end do

        ! Backward substitution U x = y
        do i = n, 1, -1
            x(i) = y(i)
            do j = i + 1, n
                x(i) = x(i) - A(i, j) * x(j)
            end do
            x(i) = x(i) / A(i, i)
        end do
    end subroutine lu_solve

end module lu_decomposition_mod
