! LU Matrix Factorization with Partial Pivoting (PA = LU)
! Standard Gaussian elimination with column pivoting in modern Fortran 2008.

program test_lu
    implicit none
    integer, parameter :: dp = kind(1.0d0)
    integer, parameter :: n = 3
    real(dp), dimension(n, n) :: A, L, U
    integer, dimension(n) :: p
    integer :: i, j, k, max_row
    real(dp) :: max_val, factor, temp

    ! Initialize test matrix A
    A(1, :) = [2.0_dp, 1.0_dp, 1.0_dp]
    A(2, :) = [4.0_dp, -6.0_dp, 0.0_dp]
    A(3, :) = [-2.0_dp, 7.0_dp, 2.0_dp]

    ! Initialize permutation vector
    do i = 1, n
        p(i) = i
    end do

    ! Gaussian elimination with partial pivoting
    do k = 1, n - 1
        ! Find pivot
        max_row = k
        max_val = abs(A(k, k))
        do i = k + 1, n
            if (abs(A(i, k)) > max_val) then
                max_val = abs(A(i, k))
                max_row = i
            end if
        end do

        ! Swap rows in A and permutation p
        if (max_row /= k) then
            do j = 1, n
                temp = A(k, j)
                A(k, j) = A(max_row, j)
                A(max_row, j) = temp
            end do
            i = p(k)
            p(k) = p(max_row)
            p(max_row) = i
        end if

        ! Compute multipliers and eliminate
        do i = k + 1, n
            factor = A(i, k) / A(k, k)
            A(i, k) = factor ! Store L multiplier in lower triangle
            do j = k + 1, n
                A(i, j) = A(i, j) - factor * A(k, j)
            end do
        end do
    end do

    print *, "[Fortran LU] Factorization converged. Pivot row 1 swapped with:", p(1)
    if (p(1) /= 2) then
        stop 1
    end if
end program test_lu
