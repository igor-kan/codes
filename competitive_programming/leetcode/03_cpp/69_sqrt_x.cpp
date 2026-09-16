#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

int sqrtX(int x) {
    int low = 0, high = x;
    while (low <= high) {
        int middle = low + (high - low) / 2;
        if (static_cast<long long>(middle) * middle <= x) low = middle + 1; else high = middle - 1;
    }
    return high;
}

int main() {
    assert(sqrtX(4) == 2 && sqrtX(8) == 2 && sqrtX(0) == 0);
    std::cout << "69 sqrt x ok\n";
    return 0;
}
