/**
 * @file errors.cpp
 * @brief Rich diagnostic error reporting for Yaroslavskiy Dual-Pivot Vectorized Quicksort.
 * Module: quicksort_dual_pivot
 */

typedef enum quicksort_dual_pivot_error {
    QUICKSORT_DUAL_PIVOT_OK = 0,
    QUICKSORT_DUAL_PIVOT_ERR_NULL = -100,
    QUICKSORT_DUAL_PIVOT_ERR_CAPACITY = -101,
    QUICKSORT_DUAL_PIVOT_ERR_CONVERGENCE = -102
} quicksort_dual_pivot_error_t;

const char* quicksort_dual_pivot_strerror(quicksort_dual_pivot_error_t err) {
    switch (err) {
        case QUICKSORT_DUAL_PIVOT_OK: return "Success";
        case QUICKSORT_DUAL_PIVOT_ERR_NULL: return "Encountered null pointer argument";
        case QUICKSORT_DUAL_PIVOT_ERR_CAPACITY: return "Capacity limit exceeded";
        case QUICKSORT_DUAL_PIVOT_ERR_CONVERGENCE: return "Numerical algorithm failed to converge";
        default: return "Unknown error";
    }
}
