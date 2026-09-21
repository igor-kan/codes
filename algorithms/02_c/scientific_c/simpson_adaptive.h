#ifndef SIMPSON_ADAPTIVE_H
#define SIMPSON_ADAPTIVE_H

typedef double (*quad_fn)(double x);

double adaptive_simpson(quad_fn f, double a, double b, double tol);

#endif
