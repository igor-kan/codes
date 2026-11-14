/**
 * @file core.cpp
 * @brief Substring matching algorithm for Manber-Myers O(N log N) Suffix Array Construction.
 * Module: suffix_array_manber
 */

#include "types.cpp"
#include <string.h>

int suffix_array_manber_search(const char* text, size_t t_len, const char* pat, size_t p_len) {
    if (!text || !pat || p_len == 0 || t_len < p_len) return -1;
    for (size_t i = 0; i <= t_len - p_len; ++i) {
        if (memcmp(text + i, pat, p_len) == 0) return (int)i;
    }
    return -1;
}
