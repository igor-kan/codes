#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_knapsack_bounded_dp_d57;
    std::vector<BoundedBundle> b_its = {{2, 15, 3}, {3, 20, 2}, {5, 45, 1}};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += bounded_knapsack_max(9, b_its);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "knapsack_bounded_dp_d57 us=" << us << " sink=" << sink << "\n";
    return 0;
}
