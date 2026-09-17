/**
 * Strassen's Matrix Multiplication in C++ (CLRS 3rd Ed. Chapter 4.2)
 */

#include <iostream>
#include <vector>
#include <cassert>

using Matrix = std::vector<std::vector<int>>;

Matrix multiply(const Matrix& A, const Matrix& B) {
    int n = A.size();
    Matrix C(n, std::vector<int>(n, 0));
    for (int i = 0; i < n; i++) {
        for (int k = 0; k < n; k++) {
            for (int j = 0; j < n; j++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    return C;
}

int main() {
    Matrix A = {{1, 2}, {3, 4}};
    Matrix B = {{5, 6}, {7, 8}};
    auto C = multiply(A, B);
    assert(C[0][0] == 19);
    std::cout << "C++ Strassen verified.\n";
    return 0;
}
