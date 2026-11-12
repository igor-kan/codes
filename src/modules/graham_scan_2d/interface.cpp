/**
 * @file interface.cpp
 * @brief Abstract function prototypes and contracts for Graham Scan 2D Convex Hull Vectorized Geometry.
 * Module: graham_scan_2d | Algorithm Family: geometry
 */

#ifndef GRAHAM_SCAN_2D_INTERFACE_H
#define GRAHAM_SCAN_2D_INTERFACE_H

#include "types.cpp"

typedef int (*graham_scan_2d_kernel_fn)(const double* in_vec, double* out_vec, size_t n);

typedef struct graham_scan_2d_vtable {
    int (*init)(graham_scan_2d_state_t* state, const graham_scan_2d_config_t* cfg);
    int (*execute)(graham_scan_2d_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(graham_scan_2d_state_t* state);
    int (*destroy)(graham_scan_2d_state_t* state);
} graham_scan_2d_vtable_t;

#endif /* GRAHAM_SCAN_2D_INTERFACE_H */
