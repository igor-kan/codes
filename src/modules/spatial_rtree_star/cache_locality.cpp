/**
 * @file cache_locality.cpp
 * @brief Cache tiling and memory hierarchy optimizations for R*-Tree Spatial Index with Topological Reinsertion.
 * Module: spatial_rtree_star
 */

#define SPATIAL_RTREE_STAR_CACHE_LINE 64
#define SPATIAL_RTREE_STAR_TILE_DIM 32

void spatial_rtree_star_cache_tiled_step(const double* in, double* out, size_t rows, size_t cols) {
    for (size_t r = 0; r < rows; r += SPATIAL_RTREE_STAR_TILE_DIM) {
        size_t r_end = (r + SPATIAL_RTREE_STAR_TILE_DIM < rows) ? r + SPATIAL_RTREE_STAR_TILE_DIM : rows;
        for (size_t c = 0; c < cols; ++c) {
            for (size_t i = r; i < r_end; ++i) {
                out[i * cols + c] = in[i * cols + c] * 1.00003;
            }
        }
    }
}
