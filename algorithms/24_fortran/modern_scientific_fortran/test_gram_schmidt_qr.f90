program test_gram_schmidt_qr
    use, intrinsic :: iso_fortran_env, only: real64, int32
    use gram_schmidt_qr_mod, only: qr_mgs
    implicit none

    integer(int32), parameter :: m = 3, n = 3
    real(real64), dimension(m, n) :: A, Q, QR
    real(real64), dimension(n, n) :: R, QtQ, eye
    real(real64) :: ortho_err, rec_err
    integer(int32) :: i

    A = reshape([12.0_real64, 6.0_real64, -4.0_real64, &
                 -51.0_real64, 167.0_real64, 24.0_real64, &
                 4.0_real64, -68.0_real64, -41.0_real64], [m, n])

    call qr_mgs(A, Q, R, m, n)

    eye = 0.0_real64
    do i = 1, n
        eye(i, i) = 1.0_real64
    end do

    QtQ = matmul(transpose(Q), Q)
    ortho_err = maxval(abs(QtQ - eye))

    QR = matmul(Q, R)
    rec_err = maxval(abs(QR - A))

    if (ortho_err > 1.0e-12_real64 .or. rec_err > 1.0e-12_real64) then
        write(*,*) "FAIL: QR errors ortho:", ortho_err, "rec:", rec_err
        stop 1
    else
        write(*,*) "PASS: QR decomposition verified"
    end if
end program test_gram_schmidt_qr
