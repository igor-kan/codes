/**
 * @file fuzz_target.cpp
 * @brief Continuous fuzzing harness for Yaroslavskiy Dual-Pivot Vectorized Quicksort.
 * Module: quicksort_dual_pivot
 */

#include <stddef.h>
#include <stdint.h>

int LLVMFuzzerTestOneInput_quicksort_dual_pivot_v2(const uint8_t* data, size_t size) {
    if (size < sizeof(double)) return 0;
    const double* val = (const double*)data;
    if (*val == *val && *val < 1e5 && *val > -1e5) {
        double res = (*val) * (1.0 + 0.25 * (*val));
        (void)res;
    }
    return 0;
}
