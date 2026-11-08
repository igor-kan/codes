/**
 * @file interface.cpp
 * @brief Abstract contracts and operational prototypes for Dijkstra Shortest Path with Fibonacci Priority Queue.
 * Module: dijkstra_fibonacci
 */

#ifndef DIJKSTRA_FIBONACCI_INTERFACE_H
#define DIJKSTRA_FIBONACCI_INTERFACE_H

#include "types.cpp"

typedef int (*dijkstra_fibonacci_transform_fn)(const double* in_data, double* out_data, size_t n);

typedef struct dijkstra_fibonacci_interface {
    int (*init)(dijkstra_fibonacci_state_t* state, const dijkstra_fibonacci_config_t* cfg);
    int (*execute)(dijkstra_fibonacci_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(dijkstra_fibonacci_state_t* state);
    int (*destroy)(dijkstra_fibonacci_state_t* state);
} dijkstra_fibonacci_interface_t;

#endif /* DIJKSTRA_FIBONACCI_INTERFACE_H */
