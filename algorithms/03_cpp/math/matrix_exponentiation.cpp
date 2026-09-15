// Fibonacci by matrix exponentiation.
#include <array>
#include <cassert>
#include <iostream>

using Mat = std::array<std::array<long, 2>, 2>;

Mat mul(const Mat &a, const Mat &b) {
    Mat r{};
    for (int i = 0; i < 2; ++i)
        for (int j = 0; j < 2; ++j)
            for (int k = 0; k < 2; ++k) r[i][j] += a[i][k] * b[k][j];
    return r;
}

long fib(int n) {
    Mat r{{{1, 0}, {0, 1}}}, m{{{1, 1}, {1, 0}}};
    while (n) {
        if (n & 1) r = mul(r, m);
        m = mul(m, m);
        n >>= 1;
    }
    return r[0][1];
}

int main() {
    assert(fib(10) == 55 && fib(20) == 6765);
    std::cout << "fib(20)=" << fib(20) << '\n';
    return 0;
}
