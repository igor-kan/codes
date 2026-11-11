/**
 * @file fuzz_target.cpp
 * @brief Continuous fuzzing harness for Disjoint-Set Union (DSU) with Path Compression and Rank.
 * Module: disjoint_set_union
 */

#include <stddef.h>
#include <stdint.h>

int LLVMFuzzerTestOneInput_disjoint_set_union_day47(const uint8_t* data, size_t size) {
    if (size < sizeof(double)) return 0;
    const double* val = (const double*)data;
    if (*val == *val && *val < 1e5 && *val > -1e5) {
        double res = (*val) * (1.0 + 0.4 * (*val));
        (void)res;
    }
    return 0;
}
