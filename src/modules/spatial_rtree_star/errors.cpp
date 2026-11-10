/**
 * @file errors.cpp
 * @brief Rich diagnostic error reporting for R*-Tree Spatial Index with Topological Reinsertion.
 * Module: spatial_rtree_star
 */

typedef enum spatial_rtree_star_error_code {
    SPATIAL_RTREE_STAR_STATUS_OK = 0,
    SPATIAL_RTREE_STAR_ERR_NULL_PTR = -10,
    SPATIAL_RTREE_STAR_ERR_OUT_OF_BOUNDS = -11,
    SPATIAL_RTREE_STAR_ERR_DIVERGENCE = -12
} spatial_rtree_star_error_code_t;

const char* spatial_rtree_star_error_message(spatial_rtree_star_error_code_t code) {
    switch (code) {
        case SPATIAL_RTREE_STAR_STATUS_OK: return "Operational success";
        case SPATIAL_RTREE_STAR_ERR_NULL_PTR: return "Null pointer argument";
        case SPATIAL_RTREE_STAR_ERR_OUT_OF_BOUNDS: return "Buffer boundary exceeded";
        case SPATIAL_RTREE_STAR_ERR_DIVERGENCE: return "Numerical divergence detected";
        default: return "Unspecified error code";
    }
}
