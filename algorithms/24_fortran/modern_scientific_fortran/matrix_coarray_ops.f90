! Modern Fortran 2018 Pure Matrix Operations
module matrix_coarray_ops_mod
    use, intrinsic :: iso_fortran_env, only: real64, int32
    implicit none
    private
    public :: frobenius_norm, trace_matrix, mat_transpose, blocked_matmul

contains

    pure function frobenius_norm(A) result(fnorm)
        real(real64), dimension(:, :), intent(in) :: A
        real(real64) :: fnorm
        fnorm = sqrt(sum(A**2))
    end function frobenius_norm

    pure function trace_matrix(A) result(tr)
        real(real64), dimension(:, :), intent(in) :: A
        real(real64) :: tr
        integer(int32) :: i, n
        n = min(size(A, 1), size(A, 2))
        tr = 0.0_real64
        do i = 1, n
            tr = tr + A(i, i)
        end do
    end function trace_matrix

    pure function mat_transpose(A) result(At)
        real(real64), dimension(:, :), intent(in) :: A
        real(real64), dimension(size(A, 2), size(A, 1)) :: At
        At = transpose(A)
    end function mat_transpose

    pure function blocked_matmul(A, B) result(C)
        real(real64), dimension(:, :), intent(in) :: A, B
        real(real64), dimension(size(A, 1), size(B, 2)) :: C
        C = matmul(A, B)
    end function blocked_matmul

end module matrix_coarray_ops_mod
