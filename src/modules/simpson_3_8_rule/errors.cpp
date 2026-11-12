/**
 * @file errors.cpp
 * @brief Domain diagnostic error codes and messages for Composite Simpson 3/8 Rule Numerical Integrator.
 * Module: simpson_3_8_rule
 */

typedef enum simpson_3_8_rule_error {
    SIMPSON_3_8_RULE_SUCCESS = 0,
    SIMPSON_3_8_RULE_ERR_INVALID_INPUT = -1,
    SIMPSON_3_8_RULE_ERR_BUFFER_OVERFLOW = -2,
    SIMPSON_3_8_RULE_ERR_CONVERGENCE_FAIL = -3
} simpson_3_8_rule_error_t;

const char* simpson_3_8_rule_str_error(simpson_3_8_rule_error_t code) {
    switch (code) {
        case SIMPSON_3_8_RULE_SUCCESS: return "Operation completed successfully";
        case SIMPSON_3_8_RULE_ERR_INVALID_INPUT: return "Input argument violates domain preconditions";
        case SIMPSON_3_8_RULE_ERR_BUFFER_OVERFLOW: return "Output buffer capacity exceeded";
        case SIMPSON_3_8_RULE_ERR_CONVERGENCE_FAIL: return "Numerical algorithm failed to converge within limit";
        default: return "Unrecognized error code";
    }
}
