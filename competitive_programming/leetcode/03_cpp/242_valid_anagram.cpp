#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

bool validAnagram(std::string s, std::string t) {
    std::sort(s.begin(), s.end());
    std::sort(t.begin(), t.end());
    return s == t;
}

int main() {
    assert(validAnagram("anagram", "nagaram") && !validAnagram("rat", "car"));
    std::cout << "242 valid anagram ok\n";
    return 0;
}
