/**
 * @file core.cpp
 * @brief Rolling polynomial hash string searching algorithm for Rabin-Karp Rolling Hash Substring Matcher.
 * Module: rabin_karp_search
 */

#include "types.cpp"
#include <string.h>
#include <stdint.h>

int rabin_karp_search_search(const char* text, size_t text_len, const char* pattern, size_t pat_len) {
    if (!text || !pattern || pat_len == 0 || text_len < pat_len) return -1;
    
    const uint64_t PRIME = 1000000007ULL;
    const uint64_t BASE = 256ULL;
    uint64_t pat_hash = 0, win_hash = 0, power = 1;

    for (size_t i = 0; i < pat_len; ++i) {
        pat_hash = (pat_hash * BASE + (uint8_t)pattern[i]) % PRIME;
        win_hash = (win_hash * BASE + (uint8_t)text[i]) % PRIME;
        if (i < pat_len - 1) power = (power * BASE) % PRIME;
    }

    for (size_t i = 0; i <= text_len - pat_len; ++i) {
        if (pat_hash == win_hash) {
            if (memcmp(text + i, pattern, pat_len) == 0) return (int)i;
        }
        if (i < text_len - pat_len) {
            win_hash = (win_hash + PRIME - ((uint8_t)text[i] * power) % PRIME) % PRIME;
            win_hash = (win_hash * BASE + (uint8_t)text[i + pat_len]) % PRIME;
        }
    }
    return -1;
}
