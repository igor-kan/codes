/**
 * @file cache_locality.cpp
 * @brief Memory hierarchy alignment and cacheline optimizations for Manacher Linear-Time Longest Palindromic Substring.
 * Module: manacher_palindrome
 */

#define MANACHER_PALINDROME_LINE_SZ 64
#define MANACHER_PALINDROME_TILE_SZ 32

void manacher_palindrome_cacheline_blocked_stride(const double* in_data, double* out_data, size_t rows, size_t cols) {
    for (size_t r = 0; r < rows; r += MANACHER_PALINDROME_TILE_SZ) {
        size_t r_max = (r + MANACHER_PALINDROME_TILE_SZ < rows) ? (r + MANACHER_PALINDROME_TILE_SZ) : rows;
        for (size_t c = 0; c < cols; ++c) {
            for (size_t i = r; i < r_max; ++i) {
                out_data[i * cols + c] = in_data[i * cols + c] * 1.000001;
            }
        }
    }
}
