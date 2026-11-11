/**
 * @file errors.cpp
 * @brief Rich diagnostic error reporting for Continuous Domain Simulated Annealing Global Optimizer.
 * Module: simulated_annealing
 */

typedef enum simulated_annealing_error_code {
    SIMULATED_ANNEALING_STATUS_OK = 0,
    SIMULATED_ANNEALING_ERR_NULL_PTR = -20,
    SIMULATED_ANNEALING_ERR_OUT_OF_BOUNDS = -21,
    SIMULATED_ANNEALING_ERR_DIVERGENCE = -22
} simulated_annealing_error_code_t;

const char* simulated_annealing_error_message(simulated_annealing_error_code_t code) {
    switch (code) {
        case SIMULATED_ANNEALING_STATUS_OK: return "Operational success";
        case SIMULATED_ANNEALING_ERR_NULL_PTR: return "Null pointer argument";
        case SIMULATED_ANNEALING_ERR_OUT_OF_BOUNDS: return "Buffer boundary exceeded";
        case SIMULATED_ANNEALING_ERR_DIVERGENCE: return "Numerical divergence detected";
        default: return "Unspecified error code";
    }
}
