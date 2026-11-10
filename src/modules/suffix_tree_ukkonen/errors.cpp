/**
 * @file errors.cpp
 * @brief Rich diagnostic error reporting for Ukkonen Linear-Time Online Suffix Tree Construction.
 * Module: suffix_tree_ukkonen
 */

typedef enum suffix_tree_ukkonen_error_code {
    SUFFIX_TREE_UKKONEN_STATUS_OK = 0,
    SUFFIX_TREE_UKKONEN_ERR_NULL_PTR = -10,
    SUFFIX_TREE_UKKONEN_ERR_OUT_OF_BOUNDS = -11,
    SUFFIX_TREE_UKKONEN_ERR_DIVERGENCE = -12
} suffix_tree_ukkonen_error_code_t;

const char* suffix_tree_ukkonen_error_message(suffix_tree_ukkonen_error_code_t code) {
    switch (code) {
        case SUFFIX_TREE_UKKONEN_STATUS_OK: return "Operational success";
        case SUFFIX_TREE_UKKONEN_ERR_NULL_PTR: return "Null pointer argument";
        case SUFFIX_TREE_UKKONEN_ERR_OUT_OF_BOUNDS: return "Buffer boundary exceeded";
        case SUFFIX_TREE_UKKONEN_ERR_DIVERGENCE: return "Numerical divergence detected";
        default: return "Unspecified error code";
    }
}
