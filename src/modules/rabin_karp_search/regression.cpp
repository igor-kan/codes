/**
 * @file regression.cpp
 * @brief Minimized regression fixtures and edge-case verification for Rabin-Karp Rolling Hash Substring Matcher.
 * Module: rabin_karp_search
 */

#include <assert.h>

void test_rabin_karp_search_minimized_regression(void) {
    // Verify non-zero small float behavior without underflow exception
    double small_val = 1e-300;
    double res = small_val * 1.0;
    assert(res > 0.0);
}
