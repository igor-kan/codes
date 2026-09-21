CXX = g++
CXXFLAGS = -Wall -Wextra -O2 -std=c++20

TESTS = test_cholesky_decomposition test_conjugate_gradient test_gaussian_quadrature \
        test_spline_interpolation test_nelder_mead_simplex test_rk45_dormand_prince \
        test_kdtree_spatial_index test_bloom_filter test_b_spline_curve test_qr_eigenvalues

all: $(TESTS)

test_cholesky_decomposition: cholesky_decomposition.cpp test_cholesky_decomposition.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

test_conjugate_gradient: conjugate_gradient.cpp test_conjugate_gradient.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

test_gaussian_quadrature: gaussian_quadrature.cpp test_gaussian_quadrature.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

test_spline_interpolation: spline_interpolation.cpp test_spline_interpolation.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

test_nelder_mead_simplex: nelder_mead_simplex.cpp test_nelder_mead_simplex.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

test_rk45_dormand_prince: rk45_dormand_prince.cpp test_rk45_dormand_prince.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

test_kdtree_spatial_index: kdtree_spatial_index.cpp test_kdtree_spatial_index.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

test_bloom_filter: bloom_filter.cpp test_bloom_filter.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

test_b_spline_curve: b_spline_curve.cpp test_b_spline_curve.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

test_qr_eigenvalues: qr_eigenvalues.cpp test_qr_eigenvalues.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

test: all
	@for t in $(TESTS); do ./$$t || exit 1; done
	@echo "All C++ unit tests PASSED."

clean:
	rm -f $(TESTS) *.o
