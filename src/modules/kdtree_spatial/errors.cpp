/**
 * @file errors.cpp
 * @brief Rich diagnostic error reporting for Multi-Dimensional K-d Tree Nearest Neighbor Engine.
 * Module: kdtree_spatial
 */

typedef enum kdtree_spatial_error {
    KDTREE_SPATIAL_OK = 0,
    KDTREE_SPATIAL_ERR_NULL = -100,
    KDTREE_SPATIAL_ERR_CAPACITY = -101,
    KDTREE_SPATIAL_ERR_CONVERGENCE = -102
} kdtree_spatial_error_t;

const char* kdtree_spatial_strerror(kdtree_spatial_error_t err) {
    switch (err) {
        case KDTREE_SPATIAL_OK: return "Success";
        case KDTREE_SPATIAL_ERR_NULL: return "Encountered null pointer argument";
        case KDTREE_SPATIAL_ERR_CAPACITY: return "Capacity limit exceeded";
        case KDTREE_SPATIAL_ERR_CONVERGENCE: return "Numerical algorithm failed to converge";
        default: return "Unknown error";
    }
}
