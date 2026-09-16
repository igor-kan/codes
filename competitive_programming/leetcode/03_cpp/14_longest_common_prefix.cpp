#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

std::string longestCommonPrefix(const std::vector<std::string> &strs) {
    if (strs.empty()) return "";
    std::string prefix = strs[0];
    for (size_t i = 1; i < strs.size(); ++i) {
        while (strs[i].compare(0, prefix.size(), prefix) != 0) {
            prefix.pop_back();
            if (prefix.empty()) return "";
        }
    }
    return prefix;
}

int main() {
    assert(longestCommonPrefix({"flower", "flow", "flight"}) == "fl");
    assert(longestCommonPrefix({"dog", "racecar", "car"}) == "");
    std::cout << "14 longest common prefix ok\n";
    return 0;
}
