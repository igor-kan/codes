#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

int reverseInteger(int x) {
    int sign = x < 0 ? -1 : 1;
    long long value = std::abs(static_cast<long long>(x));
    long long reversed = 0;
    while (value > 0) { reversed = reversed * 10 + value % 10; value /= 10; }
    reversed *= sign;
    return (reversed < -(1LL << 31) || reversed > (1LL << 31) - 1) ? 0 : static_cast<int>(reversed);
}

int main() {
    assert(reverseInteger(123) == 321 && reverseInteger(-123) == -321 && reverseInteger(120) == 21);
    assert(reverseInteger(1534236469) == 0);
    std::cout << "7 reverse integer ok\n";
    return 0;
}
