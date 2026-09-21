NVCC = nvcc
CXX = g++
CFLAGS = -Wall -Wextra -O2 -include cuda_compat.h

TESTS = test_parallel_reduction test_prefix_sum_scan test_matrix_transpose \
        test_radix_sort test_convolution_2d test_monte_carlo_option \
        test_nbody_tiling test_histogram_atomic test_sparse_spmv test_heat_diffusion

all: $(TESTS)

test_%: test_%.cu
	@which nvcc >/dev/null 2>&1 && $(NVCC) -O2 $< -o $@ || $(CXX) $(CFLAGS) -x c++ $< -o $@

test: all
	@for t in $(TESTS); do ./$$t || exit 1; done
	@echo "All CUDA parallel host tests PASSED."

clean:
	rm -f $(TESTS) *.o
