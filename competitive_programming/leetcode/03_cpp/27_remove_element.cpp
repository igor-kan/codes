#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

std::vector<int> removeElement(const std::vector<int> &nums, int value) {
    std::vector<int> result;
    for (int number : nums) if (number != value) result.push_back(number);
    return result;
}

int main() {
    assert((removeElement({3, 2, 2, 3}, 3) == std::vector<int>{2, 2}));
    assert((removeElement({0, 1, 2, 2, 3, 0, 4, 2}, 2) == std::vector<int>{0, 1, 3, 0, 4}));
    std::cout << "27 remove element ok\n";
    return 0;
}
