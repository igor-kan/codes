#ifndef COMPLEX_ARITHMETIC_H
#define COMPLEX_ARITHMETIC_H

typedef struct {
    double real;
    double imag;
} Cplx;

Cplx cplx_mul(Cplx a, Cplx b);
Cplx cplx_exp(Cplx a);

#endif
