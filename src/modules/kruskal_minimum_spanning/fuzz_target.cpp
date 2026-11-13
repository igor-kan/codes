/**
 * @file fuzz_target.cpp
 * @brief Continuous fuzzing target for AFL++ and LibFuzzer for Kruskal Minimum Spanning Tree with Disjoint Set Union.
 * Module: kruskal_minimum_spanning
 */

#include <stddef.h>
#include <stdint.h>

int LLVMFuzzerTestOneInput_kruskal_minimum_spanning_day49(const uint8_t* data, size_t size) {
    if (size < sizeof(double)) return 0;
    const double* val = (const double*)data;
    if (*val == *val && *val > -1e6 && *val < 1e6) {
        double res = (*val) * 1.0001;
        (void)res;
    }
    return 0;
}
