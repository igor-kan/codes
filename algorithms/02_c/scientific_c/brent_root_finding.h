#ifndef BRENT_ROOT_FINDING_H
#define BRENT_ROOT_FINDING_H

typedef double (*scalar_fn)(double x);

double brent_find_root(scalar_fn f, double a, double b, double tol, int max_iter);

#endif
