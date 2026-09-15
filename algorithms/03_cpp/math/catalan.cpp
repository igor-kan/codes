// Catalan numbers by the recurrence.
#include <cassert>
#include <iostream>
#include <vector>

int main() {
    std::vector<long> c(11, 0);
    c[0] = 1;
    for (int i = 1; i <= 10; ++i)
        for (int j = 0; j < i; ++j) c[i] += c[j] * c[i - 1 - j];
    assert(c[5] == 42 && c[10] == 16796);
    std::cout << "catalan(10)=" << c[10] << '\n';
    return 0;
}
