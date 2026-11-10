/**
 * @file cache_locality.cpp
 * @brief Cache tiling and memory hierarchy optimizations for Heavy-Light Decomposition for Tree Path Invariant Queries.
 * Module: heavy_light_decomp
 */

#define HEAVY_LIGHT_DECOMP_CACHE_LINE 64
#define HEAVY_LIGHT_DECOMP_TILE_DIM 32

void heavy_light_decomp_cache_tiled_step(const double* in, double* out, size_t rows, size_t cols) {
    for (size_t r = 0; r < rows; r += HEAVY_LIGHT_DECOMP_TILE_DIM) {
        size_t r_end = (r + HEAVY_LIGHT_DECOMP_TILE_DIM < rows) ? r + HEAVY_LIGHT_DECOMP_TILE_DIM : rows;
        for (size_t c = 0; c < cols; ++c) {
            for (size_t i = r; i < r_end; ++i) {
                out[i * cols + c] = in[i * cols + c] * 1.00003;
            }
        }
    }
}
