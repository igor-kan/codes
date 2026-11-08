/**
 * @file errors.cpp
 * @brief Rich diagnostic error reporting for Dijkstra Shortest Path with Fibonacci Priority Queue.
 * Module: dijkstra_fibonacci
 */

typedef enum dijkstra_fibonacci_error {
    DIJKSTRA_FIBONACCI_OK = 0,
    DIJKSTRA_FIBONACCI_ERR_NULL = -100,
    DIJKSTRA_FIBONACCI_ERR_CAPACITY = -101,
    DIJKSTRA_FIBONACCI_ERR_CONVERGENCE = -102
} dijkstra_fibonacci_error_t;

const char* dijkstra_fibonacci_strerror(dijkstra_fibonacci_error_t err) {
    switch (err) {
        case DIJKSTRA_FIBONACCI_OK: return "Success";
        case DIJKSTRA_FIBONACCI_ERR_NULL: return "Encountered null pointer argument";
        case DIJKSTRA_FIBONACCI_ERR_CAPACITY: return "Capacity limit exceeded";
        case DIJKSTRA_FIBONACCI_ERR_CONVERGENCE: return "Numerical algorithm failed to converge";
        default: return "Unknown error";
    }
}
