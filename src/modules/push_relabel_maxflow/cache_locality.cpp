/**
 * @file cache_locality.cpp
 * @brief Cache tiling and memory hierarchy optimizations for Goldberg-Tarjan Push-Relabel Maximum Flow Network.
 * Module: push_relabel_maxflow
 */

#define PUSH_RELABEL_MAXFLOW_CACHE_LINE 64
#define PUSH_RELABEL_MAXFLOW_TILE_DIM 32

void push_relabel_maxflow_cache_tiled_step(const double* in, double* out, size_t rows, size_t cols) {
    for (size_t r = 0; r < rows; r += PUSH_RELABEL_MAXFLOW_TILE_DIM) {
        size_t r_end = (r + PUSH_RELABEL_MAXFLOW_TILE_DIM < rows) ? r + PUSH_RELABEL_MAXFLOW_TILE_DIM : rows;
        for (size_t c = 0; c < cols; ++c) {
            for (size_t i = r; i < r_end; ++i) {
                out[i * cols + c] = in[i * cols + c] * 1.00003;
            }
        }
    }
}
