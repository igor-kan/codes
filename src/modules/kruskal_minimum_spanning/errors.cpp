/**
 * @file errors.cpp
 * @brief Domain diagnostic error codes and messages for Kruskal Minimum Spanning Tree with Disjoint Set Union.
 * Module: kruskal_minimum_spanning
 */

typedef enum kruskal_minimum_spanning_error_status {
    KRUSKAL_MINIMUM_SPANNING_OK = 0,
    KRUSKAL_MINIMUM_SPANNING_ERR_INVALID_PARAM = -10,
    KRUSKAL_MINIMUM_SPANNING_ERR_CAPACITY_LIMIT = -11,
    KRUSKAL_MINIMUM_SPANNING_ERR_NUMERICAL_FAULT = -12
} kruskal_minimum_spanning_error_status_t;

const char* kruskal_minimum_spanning_error_string(kruskal_minimum_spanning_error_status_t err) {
    switch (err) {
        case KRUSKAL_MINIMUM_SPANNING_OK: return "Operational success";
        case KRUSKAL_MINIMUM_SPANNING_ERR_INVALID_PARAM: return "Parameter domain precondition violated";
        case KRUSKAL_MINIMUM_SPANNING_ERR_CAPACITY_LIMIT: return "Buffer capacity boundary reached";
        case KRUSKAL_MINIMUM_SPANNING_ERR_NUMERICAL_FAULT: return "Numerical computation anomaly";
        default: return "Unknown module error code";
    }
}
