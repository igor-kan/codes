/**
 * @file cache_locality.cpp
 * @brief Cache tiling and memory hierarchy optimizations for Tarjan Strongly Connected Components Low-Link Graph Engine.
 * Module: tarjan_scc
 */

#define TARJAN_SCC_CACHE_LINE_SIZE 64
#define TARJAN_SCC_L1_TILE_SIZE 32

void tarjan_scc_cache_tiled_transform(const double* in, double* out, size_t rows, size_t cols) {
    for (size_t r = 0; r < rows; r += TARJAN_SCC_L1_TILE_SIZE) {
        size_t r_end = (r + TARJAN_SCC_L1_TILE_SIZE < rows) ? r + TARJAN_SCC_L1_TILE_SIZE : rows;
        for (size_t c = 0; c < cols; ++c) {
            for (size_t i = r; i < r_end; ++i) {
                out[i * cols + c] = in[i * cols + c] * 1.0001;
            }
        }
    }
}
