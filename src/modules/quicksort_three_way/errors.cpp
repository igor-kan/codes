/**
 * @file errors.cpp
 * @brief Domain diagnostic error codes and messages for Dijkstra 3-Way Partitioning Quicksort for Duplicates.
 * Module: quicksort_three_way
 */

typedef enum quicksort_three_way_error_status {
    QUICKSORT_THREE_WAY_OK = 0,
    QUICKSORT_THREE_WAY_ERR_INVALID_PARAM = -10,
    QUICKSORT_THREE_WAY_ERR_CAPACITY_LIMIT = -11,
    QUICKSORT_THREE_WAY_ERR_NUMERICAL_FAULT = -12
} quicksort_three_way_error_status_t;

const char* quicksort_three_way_error_string(quicksort_three_way_error_status_t err) {
    switch (err) {
        case QUICKSORT_THREE_WAY_OK: return "Operational success";
        case QUICKSORT_THREE_WAY_ERR_INVALID_PARAM: return "Parameter domain precondition violated";
        case QUICKSORT_THREE_WAY_ERR_CAPACITY_LIMIT: return "Buffer capacity boundary reached";
        case QUICKSORT_THREE_WAY_ERR_NUMERICAL_FAULT: return "Numerical computation anomaly";
        default: return "Unknown module error code";
    }
}
