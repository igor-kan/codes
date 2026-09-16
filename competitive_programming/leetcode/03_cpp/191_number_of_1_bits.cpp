#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

int numberOf1Bits(uint32_t n) {
    return __builtin_popcount(n);
}

int main() {
    assert(numberOf1Bits(11) == 3 && numberOf1Bits(128) == 1 && numberOf1Bits(4294967293u) == 31);
    std::cout << "191 number of 1 bits ok\n";
    return 0;
}
