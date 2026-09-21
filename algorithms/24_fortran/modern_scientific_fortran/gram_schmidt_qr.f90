! Modern Fortran 2018 Modified Gram-Schmidt QR Decomposition
module gram_schmidt_qr_mod
    use, intrinsic :: iso_fortran_env, only: real64, int32
    implicit none
    private
    public :: qr_mgs

contains

    subroutine qr_mgs(A, Q, R, m, n)
        integer(int32), intent(in) :: m, n
        real(real64), dimension(m, n), intent(in) :: A
        real(real64), dimension(m, n), intent(out) :: Q
        real(real64), dimension(n, n), intent(out) :: R

        integer(int32) :: i, j
        real(real64) :: col_norm

        Q = A
        R = 0.0_real64

        do i = 1, n
            col_norm = sqrt(sum(Q(:, i)**2))
            R(i, i) = col_norm
            if (col_norm > 1.0e-15_real64) then
                Q(:, i) = Q(:, i) / col_norm
            end if

            do j = i + 1, n
                R(i, j) = dot_product(Q(:, i), Q(:, j))
                Q(:, j) = Q(:, j) - R(i, j) * Q(:, i)
            end do
        end do
    end subroutine qr_mgs

end module gram_schmidt_qr_mod
