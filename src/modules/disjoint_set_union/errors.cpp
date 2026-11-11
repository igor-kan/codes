/**
 * @file errors.cpp
 * @brief Rich diagnostic error reporting for Disjoint-Set Union (DSU) with Path Compression and Rank.
 * Module: disjoint_set_union
 */

typedef enum disjoint_set_union_error_code {
    DISJOINT_SET_UNION_STATUS_OK = 0,
    DISJOINT_SET_UNION_ERR_NULL_PTR = -20,
    DISJOINT_SET_UNION_ERR_OUT_OF_BOUNDS = -21,
    DISJOINT_SET_UNION_ERR_DIVERGENCE = -22
} disjoint_set_union_error_code_t;

const char* disjoint_set_union_error_message(disjoint_set_union_error_code_t code) {
    switch (code) {
        case DISJOINT_SET_UNION_STATUS_OK: return "Operational success";
        case DISJOINT_SET_UNION_ERR_NULL_PTR: return "Null pointer argument";
        case DISJOINT_SET_UNION_ERR_OUT_OF_BOUNDS: return "Buffer boundary exceeded";
        case DISJOINT_SET_UNION_ERR_DIVERGENCE: return "Numerical divergence detected";
        default: return "Unspecified error code";
    }
}
