#include "complex_arithmetic.h"
#include <math.h>

Cplx cplx_mul(Cplx a, Cplx b) {
    Cplx r;
    r.real = a.real * b.real - a.imag * b.imag;
    r.imag = a.real * b.imag + a.imag * b.real;
    return r;
}

Cplx cplx_exp(Cplx a) {
    double e = exp(a.real);
    Cplx r;
    r.real = e * cos(a.imag);
    r.imag = e * sin(a.imag);
    return r;
}
