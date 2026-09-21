! Modern Fortran 2018 Cooley-Tukey Radix-2 Fast Fourier Transform
module radix2_fft_mod
    use, intrinsic :: iso_fortran_env, only: real64, int32
    implicit none
    private
    public :: fft_radix2

    real(real64), parameter :: PI = 3.14159265358979323846264338327950288_real64

contains

    subroutine bit_reverse_permute(x, n)
        complex(real64), dimension(:), intent(inout) :: x
        integer(int32), intent(in) :: n
        integer(int32) :: i, j, k
        complex(real64) :: temp

        j = 1
        do i = 1, n - 1
            if (i < j) then
                temp = x(i)
                x(i) = x(j)
                x(j) = temp
            end if
            k = n / 2
            do while (k >= 1 .and. k < j)
                j = j - k
                k = k / 2
            end do
            j = j + k
        end do
    end subroutine bit_reverse_permute

    subroutine fft_radix2(x, inverse)
        complex(real64), dimension(:), intent(inout) :: x
        logical, intent(in) :: inverse
        integer(int32) :: n, m, step, j, k
        real(real64) :: angle, sign_dir
        complex(real64) :: w, w_step, u, v

        n = size(x)
        call bit_reverse_permute(x, n)

        sign_dir = merge(1.0_real64, -1.0_real64, inverse)

        m = 2
        do while (m <= n)
            angle = sign_dir * 2.0_real64 * PI / real(m, real64)
            w_step = cmplx(cos(angle), sin(angle), kind=real64)
            step = m

            do k = 1, n, step
                w = cmplx(1.0_real64, 0.0_real64, kind=real64)
                do j = 0, (m / 2) - 1
                    u = x(k + j)
                    v = w * x(k + j + m / 2)
                    x(k + j) = u + v
                    x(k + j + m / 2) = u - v
                    w = w * w_step
                end do
            end do
            m = m * 2
        end do

        if (inverse) then
            x = x / real(n, real64)
        end if
    end subroutine fft_radix2

end module radix2_fft_mod
