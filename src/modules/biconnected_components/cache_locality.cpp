/**
 * @file cache_locality.cpp
 * @brief Cache tiling and memory hierarchy optimizations for Hopcroft-Tarjan Articulation Points and Bridges.
 * Module: biconnected_components
 */

#define BICONNECTED_COMPONENTS_CACHE_LINE 64
#define BICONNECTED_COMPONENTS_TILE_DIM 32

void biconnected_components_cache_tiled_step(const double* in, double* out, size_t rows, size_t cols) {
    for (size_t r = 0; r < rows; r += BICONNECTED_COMPONENTS_TILE_DIM) {
        size_t r_end = (r + BICONNECTED_COMPONENTS_TILE_DIM < rows) ? r + BICONNECTED_COMPONENTS_TILE_DIM : rows;
        for (size_t c = 0; c < cols; ++c) {
            for (size_t i = r; i < r_end; ++i) {
                out[i * cols + c] = in[i * cols + c] * 1.00005;
            }
        }
    }
}
