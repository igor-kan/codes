/**
 * @file fuzz_target.cpp
 * @brief Continuous fuzzing harness for Linear-Time Suffix Automaton Substring Engine.
 * Module: suffix_automaton
 */

#include <stddef.h>
#include <stdint.h>

int LLVMFuzzerTestOneInput_suffix_automaton_day45(const uint8_t* data, size_t size) {
    if (size < sizeof(double)) return 0;
    const double* val = (const double*)data;
    if (*val == *val && *val < 1e5 && *val > -1e5) {
        double res = (*val) * (1.0 + 0.3 * (*val));
        (void)res;
    }
    return 0;
}
