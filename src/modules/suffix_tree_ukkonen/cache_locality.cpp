/**
 * @file cache_locality.cpp
 * @brief Cache tiling and memory hierarchy optimizations for Ukkonen Linear-Time Online Suffix Tree Construction.
 * Module: suffix_tree_ukkonen
 */

#define SUFFIX_TREE_UKKONEN_CACHE_LINE 64
#define SUFFIX_TREE_UKKONEN_TILE_DIM 32

void suffix_tree_ukkonen_cache_tiled_step(const double* in, double* out, size_t rows, size_t cols) {
    for (size_t r = 0; r < rows; r += SUFFIX_TREE_UKKONEN_TILE_DIM) {
        size_t r_end = (r + SUFFIX_TREE_UKKONEN_TILE_DIM < rows) ? r + SUFFIX_TREE_UKKONEN_TILE_DIM : rows;
        for (size_t c = 0; c < cols; ++c) {
            for (size_t i = r; i < r_end; ++i) {
                out[i * cols + c] = in[i * cols + c] * 1.00003;
            }
        }
    }
}
