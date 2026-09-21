# Modern Fortran 2018 Makefile
FC = gfortran
FFLAGS = -O2 -std=f2018 -Wall -Wextra

MODULE_SRCS = rk4_integrator.f90 radix2_fft.f90 thomas_tridiagonal.f90 simpson_quadrature.f90 \
              conjugate_gradient.f90 matrix_coarray_ops.f90 monte_carlo_integration.f90 \
              lu_decomposition.f90 cubic_spline.f90 bisection_root.f90 \
              cholesky_factorization.f90 gram_schmidt_qr.f90 golden_section_search.f90 \
              heat_equation_explicit.f90 polynomial_roots_companion.f90

TEST_SRCS = test_rk4_integrator.f90 test_radix2_fft.f90 test_thomas_tridiagonal.f90 test_simpson_quadrature.f90 \
            test_conjugate_gradient.f90 test_matrix_coarray_ops.f90 test_monte_carlo_integration.f90 \
            test_lu_decomposition.f90 test_cubic_spline.f90 test_bisection_root.f90 \
            test_cholesky_factorization.f90 test_gram_schmidt_qr.f90 test_golden_section_search.f90 \
            test_heat_equation_explicit.f90 test_polynomial_roots_companion.f90

TEST_BINS = $(TEST_SRCS:.f90=.out)

all: test

test: $(TEST_BINS)
	@for t in $(TEST_BINS); do \
		echo "Running $$t..."; \
		./$$t || exit 1; \
	done

%.out: %.f90 $(MODULE_SRCS)
	$(FC) $(FFLAGS) -o $@ $(MODULE_SRCS) $<

clean:
	rm -f *.o *.mod *.out
