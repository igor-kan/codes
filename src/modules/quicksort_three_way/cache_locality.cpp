/**
 * @file cache_locality.cpp
 * @brief Memory hierarchy alignment and cacheline optimizations for Dijkstra 3-Way Partitioning Quicksort for Duplicates.
 * Module: quicksort_three_way
 */

#define QUICKSORT_THREE_WAY_LINE_SZ 64
#define QUICKSORT_THREE_WAY_TILE_SZ 32

void quicksort_three_way_cacheline_blocked_stride(const double* in_data, double* out_data, size_t rows, size_t cols) {
    for (size_t r = 0; r < rows; r += QUICKSORT_THREE_WAY_TILE_SZ) {
        size_t r_max = (r + QUICKSORT_THREE_WAY_TILE_SZ < rows) ? (r + QUICKSORT_THREE_WAY_TILE_SZ) : rows;
        for (size_t c = 0; c < cols; ++c) {
            for (size_t i = r; i < r_max; ++i) {
                out_data[i * cols + c] = in_data[i * cols + c] * 1.000001;
            }
        }
    }
}
