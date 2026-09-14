/**
 * Z-algorithm: z[i] = length of the longest substring starting at i
 * that is also a prefix of s.
 */

#include <string>
#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>

std::vector<int> zFunction(const std::string& s) {
    int n = static_cast<int>(s.size());
    std::vector<int> z(n, 0);
    int l = 0, r = 0;
    for (int i = 1; i < n; ++i) {
        if (i <= r) z[i] = std::min(r - i + 1, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) ++z[i];
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    return z;
}

int main() {
    auto z = zFunction("aaaaa");
    assert((z == std::vector<int>{0, 4, 3, 2, 1}));

    auto z2 = zFunction("abacaba");
    assert((z2 == std::vector<int>{0, 0, 1, 0, 3, 0, 1}));
    std::cout << "[C++ ZAlgorithm] Z-function verified." << std::endl;
    return 0;
}
