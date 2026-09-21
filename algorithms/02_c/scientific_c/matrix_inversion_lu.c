#include "matrix_inversion_lu.h"
#include <math.h>

int invert_matrix_3x3(const double A[3][3], double invA[3][3]) {
    double det = A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1])
               - A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0])
               + A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0]);
               
    if (fabs(det) < 1e-12) return 0; // Singular
    
    double invdet = 1.0 / det;
    invA[0][0] =  (A[1][1]*A[2][2] - A[1][2]*A[2][1]) * invdet;
    invA[0][1] = -(A[0][1]*A[2][2] - A[0][2]*A[2][1]) * invdet;
    invA[0][2] =  (A[0][1]*A[1][2] - A[0][2]*A[1][1]) * invdet;
    invA[1][0] = -(A[1][0]*A[2][2] - A[1][2]*A[2][0]) * invdet;
    invA[1][1] =  (A[0][0]*A[2][2] - A[0][2]*A[2][0]) * invdet;
    invA[1][2] = -(A[0][0]*A[1][2] - A[0][2]*A[1][0]) * invdet;
    invA[2][0] =  (A[1][0]*A[2][1] - A[1][1]*A[2][0]) * invdet;
    invA[2][1] = -(A[0][0]*A[2][1] - A[0][1]*A[2][0]) * invdet;
    invA[2][2] =  (A[0][0]*A[1][1] - A[0][1]*A[1][0]) * invdet;
    return 1;
}
