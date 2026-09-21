CC = gcc
CFLAGS = -Wall -Wextra -O2 -std=c11 -D_DEFAULT_SOURCE -D_GNU_SOURCE
LDFLAGS = -lm

TESTS = test_rk4_integrator test_fast_fourier_transform test_matrix_inversion_lu         test_brent_root_finding test_simpson_adaptive test_quaternion_kinematics         test_complex_arithmetic test_polynomial_roots_laguerre test_sparse_matrix_csr         test_monte_carlo_pi test_levenshtein_distance test_sha256_digest         test_convex_hull_graham test_huffman_coding test_dijkstra_shortest_path

all: $(TESTS)

test_rk4_integrator: rk4_integrator.c test_rk4_integrator.c
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)

test_fast_fourier_transform: fast_fourier_transform.c test_fast_fourier_transform.c
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)

test_matrix_inversion_lu: matrix_inversion_lu.c test_matrix_inversion_lu.c
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)

test_brent_root_finding: brent_root_finding.c test_brent_root_finding.c
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)

test_simpson_adaptive: simpson_adaptive.c test_simpson_adaptive.c
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)

test_quaternion_kinematics: quaternion_kinematics.c test_quaternion_kinematics.c
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)

test_complex_arithmetic: complex_arithmetic.c test_complex_arithmetic.c
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)

test_polynomial_roots_laguerre: polynomial_roots_laguerre.c test_polynomial_roots_laguerre.c
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)

test_sparse_matrix_csr: sparse_matrix_csr.c test_sparse_matrix_csr.c
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)

test_monte_carlo_pi: monte_carlo_pi.c test_monte_carlo_pi.c
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)

test_levenshtein_distance: levenshtein_distance.c test_levenshtein_distance.c
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)

test_sha256_digest: sha256_digest.c test_sha256_digest.c
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)

test_convex_hull_graham: convex_hull_graham.c test_convex_hull_graham.c
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)

test_huffman_coding: huffman_coding.c test_huffman_coding.c
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)

test_dijkstra_shortest_path: dijkstra_shortest_path.c test_dijkstra_shortest_path.c
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)

test: all
	@for t in $(TESTS); do ./$$t || exit 1; done
	@echo "All C unit tests PASSED."

clean:
	rm -f $(TESTS) *.o
