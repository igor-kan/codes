/**
 * @file errors.cpp
 * @brief Domain diagnostic error codes and messages for Leaf-Chained B+ Tree Index Structure for Range Scans.
 * Module: b_plus_tree_leaf
 */

typedef enum b_plus_tree_leaf_error_status {
    B_PLUS_TREE_LEAF_OK = 0,
    B_PLUS_TREE_LEAF_ERR_INVALID_PARAM = -10,
    B_PLUS_TREE_LEAF_ERR_CAPACITY_LIMIT = -11,
    B_PLUS_TREE_LEAF_ERR_NUMERICAL_FAULT = -12
} b_plus_tree_leaf_error_status_t;

const char* b_plus_tree_leaf_error_string(b_plus_tree_leaf_error_status_t err) {
    switch (err) {
        case B_PLUS_TREE_LEAF_OK: return "Operational success";
        case B_PLUS_TREE_LEAF_ERR_INVALID_PARAM: return "Parameter domain precondition violated";
        case B_PLUS_TREE_LEAF_ERR_CAPACITY_LIMIT: return "Buffer capacity boundary reached";
        case B_PLUS_TREE_LEAF_ERR_NUMERICAL_FAULT: return "Numerical computation anomaly";
        default: return "Unknown module error code";
    }
}
