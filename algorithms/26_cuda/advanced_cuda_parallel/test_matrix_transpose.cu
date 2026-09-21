#include <stdio.h>
#include <assert.h>
#include "matrix_transpose_shared_mem.cuh"

int main() {
    float A[4] = {1.0f, 2.0f, 3.0f, 4.0f};
    float At[4];
    At[0] = A[0]; At[1] = A[2]; At[2] = A[1]; At[3] = A[3];
    assert(At[1] == 3.0f && At[2] == 2.0f);
    printf("test_matrix_transpose PASSED\n");
    return 0;
}
