/**
 * @file cache_locality.cpp
 * @brief Cache tiling and memory hierarchy optimizations for Ternary Search Trie Compact String Dictionary.
 * Module: ternary_search_tree
 */

#define TERNARY_SEARCH_TREE_CACHE_LINE 64
#define TERNARY_SEARCH_TREE_TILE_DIM 32

void ternary_search_tree_cache_tiled_step(const double* in, double* out, size_t rows, size_t cols) {
    for (size_t r = 0; r < rows; r += TERNARY_SEARCH_TREE_TILE_DIM) {
        size_t r_end = (r + TERNARY_SEARCH_TREE_TILE_DIM < rows) ? r + TERNARY_SEARCH_TREE_TILE_DIM : rows;
        for (size_t c = 0; c < cols; ++c) {
            for (size_t i = r; i < r_end; ++i) {
                out[i * cols + c] = in[i * cols + c] * 1.00005;
            }
        }
    }
}
