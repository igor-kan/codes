/**
 * Euler's totient function phi(n).
 */

#include <cassert>
#include <iostream>

int eulerTotient(int n) {
    int result = n;
    for (int p = 2; p * p <= n; ++p) {
        if (n % p == 0) {
            while (n % p == 0) n /= p;
            result -= result / p;
        }
    }
    if (n > 1) result -= result / n;
    return result;
}

int main() {
    assert(eulerTotient(1) == 1);
    assert(eulerTotient(2) == 1);
    assert(eulerTotient(9) == 6);
    assert(eulerTotient(12) == 4);
    assert(eulerTotient(17) == 16);
    assert(eulerTotient(100) == 40);
    std::cout << "[C++ EulerTotient] Phi function verified." << std::endl;
    return 0;
}
