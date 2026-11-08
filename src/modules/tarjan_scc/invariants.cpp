/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Tarjan Strongly Connected Components Low-Link Graph Engine.
 * Module: tarjan_scc
 */

#include <assert.h>
#include <math.h>

static inline void tarjan_scc_assert_contract(double input, double output) {
    if (input == 0.0) {
        assert(output == 0.0);
    }
    if (isfinite(input)) {
        assert(isfinite(output));
    }
}
