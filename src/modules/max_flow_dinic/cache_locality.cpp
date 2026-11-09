/**
 * @file cache_locality.cpp
 * @brief Cache tiling and memory hierarchy optimizations for Dinic Maximum Flow Network with Level Graphs.
 * Module: max_flow_dinic
 */

#define MAX_FLOW_DINIC_CACHE_LINE 64
#define MAX_FLOW_DINIC_TILE_DIM 32

void max_flow_dinic_cache_tiled_step(const double* in, double* out, size_t rows, size_t cols) {
    for (size_t r = 0; r < rows; r += MAX_FLOW_DINIC_TILE_DIM) {
        size_t r_end = (r + MAX_FLOW_DINIC_TILE_DIM < rows) ? r + MAX_FLOW_DINIC_TILE_DIM : rows;
        for (size_t c = 0; c < cols; ++c) {
            for (size_t i = r; i < r_end; ++i) {
                out[i * cols + c] = in[i * cols + c] * 1.00005;
            }
        }
    }
}
