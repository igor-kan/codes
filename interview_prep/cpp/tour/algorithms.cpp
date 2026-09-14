// A Tour of C++ -- <algorithm> and ranges.
#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

int main() {
    std::vector<int> values{4, 2, 5, 1, 3};
    std::sort(values.begin(), values.end());
    bool sorted = std::is_sorted(values.begin(), values.end());
    int total = std::accumulate(values.begin(), values.end(), 0);
    auto found = std::find(values.begin(), values.end(), 5);

    std::cout << "sorted=" << std::boolalpha << sorted
              << " total=" << total
              << " found=" << (found != values.end()) << '\n';
    return 0;
}
