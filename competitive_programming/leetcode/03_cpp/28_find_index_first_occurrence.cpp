#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

int strStr(const std::string &haystack, const std::string &needle) {
    auto position = haystack.find(needle);
    return position == std::string::npos ? -1 : static_cast<int>(position);
}

int main() {
    assert(strStr("sadbutsad", "sad") == 0 && strStr("leetcode", "leeto") == -1);
    std::cout << "28 find index first occurrence ok\n";
    return 0;
}
