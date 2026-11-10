/**
 * @file errors.cpp
 * @brief Rich diagnostic error reporting for Goldberg-Tarjan Push-Relabel Maximum Flow Network.
 * Module: push_relabel_maxflow
 */

typedef enum push_relabel_maxflow_error_code {
    PUSH_RELABEL_MAXFLOW_STATUS_OK = 0,
    PUSH_RELABEL_MAXFLOW_ERR_NULL_PTR = -10,
    PUSH_RELABEL_MAXFLOW_ERR_OUT_OF_BOUNDS = -11,
    PUSH_RELABEL_MAXFLOW_ERR_DIVERGENCE = -12
} push_relabel_maxflow_error_code_t;

const char* push_relabel_maxflow_error_message(push_relabel_maxflow_error_code_t code) {
    switch (code) {
        case PUSH_RELABEL_MAXFLOW_STATUS_OK: return "Operational success";
        case PUSH_RELABEL_MAXFLOW_ERR_NULL_PTR: return "Null pointer argument";
        case PUSH_RELABEL_MAXFLOW_ERR_OUT_OF_BOUNDS: return "Buffer boundary exceeded";
        case PUSH_RELABEL_MAXFLOW_ERR_DIVERGENCE: return "Numerical divergence detected";
        default: return "Unspecified error code";
    }
}
