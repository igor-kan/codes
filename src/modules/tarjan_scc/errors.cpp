/**
 * @file errors.cpp
 * @brief Rich diagnostic error reporting for Tarjan Strongly Connected Components Low-Link Graph Engine.
 * Module: tarjan_scc
 */

typedef enum tarjan_scc_error {
    TARJAN_SCC_OK = 0,
    TARJAN_SCC_ERR_NULL = -100,
    TARJAN_SCC_ERR_CAPACITY = -101,
    TARJAN_SCC_ERR_CONVERGENCE = -102
} tarjan_scc_error_t;

const char* tarjan_scc_strerror(tarjan_scc_error_t err) {
    switch (err) {
        case TARJAN_SCC_OK: return "Success";
        case TARJAN_SCC_ERR_NULL: return "Encountered null pointer argument";
        case TARJAN_SCC_ERR_CAPACITY: return "Capacity limit exceeded";
        case TARJAN_SCC_ERR_CONVERGENCE: return "Numerical algorithm failed to converge";
        default: return "Unknown error";
    }
}
