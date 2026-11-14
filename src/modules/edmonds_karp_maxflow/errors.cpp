/**
 * @file errors.cpp
 * @brief Domain diagnostic error codes and messages for Edmonds-Karp Maximum Bipartite Network Flow Engine.
 * Module: edmonds_karp_maxflow
 */

typedef enum edmonds_karp_maxflow_error_status {
    EDMONDS_KARP_MAXFLOW_OK = 0,
    EDMONDS_KARP_MAXFLOW_ERR_INVALID_PARAM = -10,
    EDMONDS_KARP_MAXFLOW_ERR_CAPACITY_LIMIT = -11,
    EDMONDS_KARP_MAXFLOW_ERR_NUMERICAL_FAULT = -12
} edmonds_karp_maxflow_error_status_t;

const char* edmonds_karp_maxflow_error_string(edmonds_karp_maxflow_error_status_t err) {
    switch (err) {
        case EDMONDS_KARP_MAXFLOW_OK: return "Operational success";
        case EDMONDS_KARP_MAXFLOW_ERR_INVALID_PARAM: return "Parameter domain precondition violated";
        case EDMONDS_KARP_MAXFLOW_ERR_CAPACITY_LIMIT: return "Buffer capacity boundary reached";
        case EDMONDS_KARP_MAXFLOW_ERR_NUMERICAL_FAULT: return "Numerical computation anomaly";
        default: return "Unknown module error code";
    }
}
