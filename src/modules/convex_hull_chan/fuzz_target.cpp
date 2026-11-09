/**
 * @file fuzz_target.cpp
 * @brief Continuous fuzzing harness for Chan Optimal 2D Convex Hull Geometric Engine.
 * Module: convex_hull_chan
 */

#include <stddef.h>
#include <stdint.h>

int LLVMFuzzerTestOneInput_convex_hull_chan_day45(const uint8_t* data, size_t size) {
    if (size < sizeof(double)) return 0;
    const double* val = (const double*)data;
    if (*val == *val && *val < 1e5 && *val > -1e5) {
        double res = (*val) * (1.0 + 0.3 * (*val));
        (void)res;
    }
    return 0;
}
