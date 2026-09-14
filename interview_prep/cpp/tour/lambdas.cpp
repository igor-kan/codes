// A Tour of C++ -- lambdas and capture modes.
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::vector<int> values{1, 2, 3, 4, 5, 6};
    int threshold = 3;

    auto evens = std::count_if(values.begin(), values.end(),
                               [](int n) { return n % 2 == 0; });
    auto above = std::count_if(values.begin(), values.end(),
                               [threshold](int n) { return n > threshold; });

    int multiplier = 2;
    std::for_each(values.begin(), values.end(), [&](int &n) { n *= multiplier; });

    std::cout << "evens=" << evens << " above=" << above
              << " first=" << values.front() << '\n';
    return 0;
}
