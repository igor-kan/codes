program test_polynomial_roots_companion
    use, intrinsic :: iso_fortran_env, only: real64, int32
    use polynomial_roots_companion_mod, only: horner_eval, newton_poly_root
    implicit none

    integer(int32), parameter :: deg = 2
    real(real64), dimension(deg + 1) :: coeffs
    real(real64) :: root, err
    integer(int32) :: iters, status

    ! P(x) = x^2 - 4 = (x - 2)(x + 2) -> c0 = -4, c1 = 0, c2 = 1
    coeffs = [-4.0_real64, 0.0_real64, 1.0_real64]

    call newton_poly_root(coeffs, deg, 1.5_real64, 1.0e-10_real64, 50, root, iters, status)
    err = abs(root - 2.0_real64)

    if (err > 1.0e-9_real64) then
        write(*,*) "FAIL: Polynomial root error too large:", err
        stop 1
    else
        write(*,*) "PASS: Polynomial root found:", root, "in", iters, "iters"
    end if
end program test_polynomial_roots_companion
