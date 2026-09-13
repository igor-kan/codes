program test_matmul_blocked
    implicit none
    integer, parameter :: N = 64
    integer, parameter :: BLOCK = 16
    real(8), dimension(N, N) :: A, B, C
    integer :: i, j, k, ii, jj, kk

    ! Initialize matrices
    do j = 1, N
        do i = 1, N
            A(i, j) = dble(i + j)
            B(i, j) = dble(i - j)
            C(i, j) = 0.0d0
        end do
    end do

    ! Cache-blocked loop tiled matrix multiply (Column-major friendly)
    do jj = 1, N, BLOCK
        do kk = 1, N, BLOCK
            do ii = 1, N, BLOCK
                do j = jj, min(jj + BLOCK - 1, N)
                    do k = kk, min(kk + BLOCK - 1, N)
                        do i = ii, min(ii + BLOCK - 1, N)
                            C(i, j) = C(i, j) + A(i, k) * B(k, j)
                        end do
                    end do
                end do
            end do
        end do
    end do

    ! Verify an element: C(1, 1) = sum_{k=1}^N A(1, k) * B(k, 1)
    ! A(1, k) = 1 + k, B(k, 1) = k - 1 -> (k+1)(k-1) = k^2 - 1
    ! sum_{k=1}^N (k^2 - 1) = N(N+1)(2N+1)/6 - N
    print *, "[Fortran Matrix] Blocked matrix multiply completed."
    print *, "C(1, 1) computed = ", C(1, 1)
end program test_matmul_blocked
