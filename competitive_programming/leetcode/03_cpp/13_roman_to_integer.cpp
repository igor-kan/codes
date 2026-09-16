#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

int romanToInteger(const std::string &text) {
    auto value = [](char c) {
        switch (c) {
            case 'I': return 1; case 'V': return 5; case 'X': return 10;
            case 'L': return 50; case 'C': return 100; case 'D': return 500; default: return 1000;
        }
    };
    int total = 0;
    for (size_t i = 0; i < text.size(); ++i) {
        int current = value(text[i]);
        if (i + 1 < text.size() && current < value(text[i + 1])) total -= current;
        else total += current;
    }
    return total;
}

int main() {
    assert(romanToInteger("III") == 3 && romanToInteger("LVIII") == 58 && romanToInteger("MCMXCIV") == 1994);
    std::cout << "13 roman to integer ok\n";
    return 0;
}
