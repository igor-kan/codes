program test_radix2_fft
    use, intrinsic :: iso_fortran_env, only: real64, int32
    use radix2_fft_mod, only: fft_radix2
    implicit none

    integer(int32), parameter :: n = 16
    complex(real64), dimension(n) :: x_orig, x_fft
    real(real64) :: max_err
    integer(int32) :: i

    do i = 1, n
        x_orig(i) = cmplx(sin(real(i, real64) * 0.4_real64), cos(real(i, real64) * 0.2_real64), kind=real64)
    end do

    x_fft = x_orig
    call fft_radix2(x_fft, .false.)
    call fft_radix2(x_fft, .true.)

    max_err = maxval(abs(x_fft - x_orig))

    if (max_err > 1.0e-12_real64) then
        write(*,*) "FAIL: FFT roundtrip max error:", max_err
        stop 1
    else
        write(*,*) "PASS: Radix-2 FFT roundtrip error:", max_err
    end if
end program test_radix2_fft
