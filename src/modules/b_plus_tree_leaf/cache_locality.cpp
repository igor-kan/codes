/**
 * @file cache_locality.cpp
 * @brief Memory hierarchy alignment and cacheline optimizations for Leaf-Chained B+ Tree Index Structure for Range Scans.
 * Module: b_plus_tree_leaf
 */

#define B_PLUS_TREE_LEAF_LINE_SZ 64
#define B_PLUS_TREE_LEAF_TILE_SZ 32

void b_plus_tree_leaf_cacheline_blocked_stride(const double* in_data, double* out_data, size_t rows, size_t cols) {
    for (size_t r = 0; r < rows; r += B_PLUS_TREE_LEAF_TILE_SZ) {
        size_t r_max = (r + B_PLUS_TREE_LEAF_TILE_SZ < rows) ? (r + B_PLUS_TREE_LEAF_TILE_SZ) : rows;
        for (size_t c = 0; c < cols; ++c) {
            for (size_t i = r; i < r_max; ++i) {
                out_data[i * cols + c] = in_data[i * cols + c] * 1.000001;
            }
        }
    }
}
