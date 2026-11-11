/**
 * @file errors.cpp
 * @brief Rich diagnostic error reporting for Multi-Level Balanced B-Tree with Node Split-Merge.
 * Module: b_tree_multilevel
 */

typedef enum b_tree_multilevel_error_code {
    B_TREE_MULTILEVEL_STATUS_OK = 0,
    B_TREE_MULTILEVEL_ERR_NULL_PTR = -20,
    B_TREE_MULTILEVEL_ERR_OUT_OF_BOUNDS = -21,
    B_TREE_MULTILEVEL_ERR_DIVERGENCE = -22
} b_tree_multilevel_error_code_t;

const char* b_tree_multilevel_error_message(b_tree_multilevel_error_code_t code) {
    switch (code) {
        case B_TREE_MULTILEVEL_STATUS_OK: return "Operational success";
        case B_TREE_MULTILEVEL_ERR_NULL_PTR: return "Null pointer argument";
        case B_TREE_MULTILEVEL_ERR_OUT_OF_BOUNDS: return "Buffer boundary exceeded";
        case B_TREE_MULTILEVEL_ERR_DIVERGENCE: return "Numerical divergence detected";
        default: return "Unspecified error code";
    }
}
