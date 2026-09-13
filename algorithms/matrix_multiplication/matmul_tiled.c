#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#define N 64
#define TILE 16

void matmul_tiled(const double *A, const double *B, double *C, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            C[i * n + j] = 0.0;
        }
    }

    for (int ii = 0; ii < n; ii += TILE) {
        for (int kk = 0; kk < n; kk += TILE) {
            for (int jj = 0; jj < n; jj += TILE) {
                for (int i = ii; i < ii + TILE && i < n; i++) {
                    for (int k = kk; k < kk + TILE && k < n; k++) {
                        double a_ik = A[i * n + k];
                        for (int j = jj; j < jj + TILE && j < n; j++) {
                            C[i * n + j] += a_ik * B[k * n + j];
                        }
                    }
                }
            }
        }
    }
}

int main(void) {
    double *A = (double *)malloc(N * N * sizeof(double));
    double *B = (double *)malloc(N * N * sizeof(double));
    double *C = (double *)malloc(N * N * sizeof(double));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            A[i * N + j] = (double)(i + 1);
            B[i * N + j] = (i == j) ? 1.0 : 0.0; // Identity matrix
        }
    }

    matmul_tiled(A, B, C, N);

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            assert(C[i * N + j] == A[i * N + j]);
        }
    }
    printf("[C Matrix] Tiled matrix multiplication verified against identity.\n");

    free(A);
    free(B);
    free(C);
    return 0;
}
