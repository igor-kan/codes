// LSD radix sort for non-negative integers.
#include <algorithm>
#include <array>
#include <cstddef>
#include <iostream>
#include <vector>

void radix_sort(std::vector<int> &values) {
    if (values.empty()) return;
    const int max_value = *std::max_element(values.begin(), values.end());
    for (int exp = 1; max_value / exp > 0; exp *= 10) {
        std::array<std::vector<int>, 10> buckets;
        for (int value : values) buckets[(value / exp) % 10].push_back(value);
        std::size_t index = 0;
        for (auto &bucket : buckets)
            for (int value : bucket) values[index++] = value;
    }
}

int main() {
    std::vector<int> data{170, 45, 75, 90, 802, 24, 2, 66};
    radix_sort(data);
    for (int value : data) std::cout << value << ' ';
    std::cout << '\n';
    return std::is_sorted(data.begin(), data.end()) ? 0 : 1;
}
