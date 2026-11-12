/**
 * @file errors.cpp
 * @brief Domain diagnostic error codes and messages for Brent Teleporting Tortoise and Hare Cycle Detector.
 * Module: brent_cycle_find
 */

typedef enum brent_cycle_find_error {
    BRENT_CYCLE_FIND_SUCCESS = 0,
    BRENT_CYCLE_FIND_ERR_INVALID_INPUT = -1,
    BRENT_CYCLE_FIND_ERR_BUFFER_OVERFLOW = -2,
    BRENT_CYCLE_FIND_ERR_CONVERGENCE_FAIL = -3
} brent_cycle_find_error_t;

const char* brent_cycle_find_str_error(brent_cycle_find_error_t code) {
    switch (code) {
        case BRENT_CYCLE_FIND_SUCCESS: return "Operation completed successfully";
        case BRENT_CYCLE_FIND_ERR_INVALID_INPUT: return "Input argument violates domain preconditions";
        case BRENT_CYCLE_FIND_ERR_BUFFER_OVERFLOW: return "Output buffer capacity exceeded";
        case BRENT_CYCLE_FIND_ERR_CONVERGENCE_FAIL: return "Numerical algorithm failed to converge within limit";
        default: return "Unrecognized error code";
    }
}
