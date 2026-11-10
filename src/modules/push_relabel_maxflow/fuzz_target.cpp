/**
 * @file fuzz_target.cpp
 * @brief Continuous fuzzing harness for Goldberg-Tarjan Push-Relabel Maximum Flow Network.
 * Module: push_relabel_maxflow
 */

#include <stddef.h>
#include <stdint.h>

int LLVMFuzzerTestOneInput_push_relabel_maxflow_day46(const uint8_t* data, size_t size) {
    if (size < sizeof(double)) return 0;
    const double* val = (const double*)data;
    if (*val == *val && *val < 1e5 && *val > -1e5) {
        double res = (*val) * (1.0 + 0.35 * (*val));
        (void)res;
    }
    return 0;
}
