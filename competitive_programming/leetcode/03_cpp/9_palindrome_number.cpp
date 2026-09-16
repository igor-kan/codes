#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

bool palindromeNumber(int x) {
    if (x < 0) return false;
    std::string digits = std::to_string(x);
    return std::equal(digits.begin(), digits.begin() + digits.size() / 2, digits.rbegin());
}

int main() {
    assert(palindromeNumber(121) && !palindromeNumber(-121) && !palindromeNumber(10));
    std::cout << "9 palindrome number ok\n";
    return 0;
}
