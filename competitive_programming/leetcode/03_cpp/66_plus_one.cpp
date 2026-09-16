#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

std::vector<int> plusOne(std::vector<int> digits) {
    for (int i = static_cast<int>(digits.size()) - 1; i >= 0; --i) {
        if (digits[i] < 9) { digits[i] += 1; return digits; }
        digits[i] = 0;
    }
    digits.insert(digits.begin(), 1);
    return digits;
}

int main() {
    assert((plusOne({1, 2, 3}) == std::vector<int>{1, 2, 4}));
    assert((plusOne({9, 9}) == std::vector<int>{1, 0, 0}));
    std::cout << "66 plus one ok\n";
    return 0;
}
