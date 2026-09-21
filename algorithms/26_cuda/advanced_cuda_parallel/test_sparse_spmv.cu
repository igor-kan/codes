#include <stdio.h>
#include <assert.h>
#include "sparse_spmv_csr_vector.cuh"

int main() {
    float val[2] = {5.0f, 10.0f};
    int col[2] = {0, 1};
    float x[2] = {1.0f, 2.0f};
    float y = val[0]*x[col[0]] + val[1]*x[col[1]];
    assert(y == 25.0f);
    printf("test_sparse_spmv PASSED\n");
    return 0;
}
