/**
 * @file cache_locality.cpp
 * @brief Cache tiling and memory hierarchy optimizations for Multi-Dimensional K-d Tree Nearest Neighbor Engine.
 * Module: kdtree_spatial
 */

#define KDTREE_SPATIAL_CACHE_LINE_SIZE 64
#define KDTREE_SPATIAL_L1_TILE_SIZE 32

void kdtree_spatial_cache_tiled_transform(const double* in, double* out, size_t rows, size_t cols) {
    for (size_t r = 0; r < rows; r += KDTREE_SPATIAL_L1_TILE_SIZE) {
        size_t r_end = (r + KDTREE_SPATIAL_L1_TILE_SIZE < rows) ? r + KDTREE_SPATIAL_L1_TILE_SIZE : rows;
        for (size_t c = 0; c < cols; ++c) {
            for (size_t i = r; i < r_end; ++i) {
                out[i * cols + c] = in[i * cols + c] * 1.0001;
            }
        }
    }
}
