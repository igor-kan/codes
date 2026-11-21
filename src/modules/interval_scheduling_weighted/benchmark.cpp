#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_interval_scheduling_weighted;
    std::vector<WeightedJob> b_jobs = {{0, 2, 10}, {1, 4, 25}, {3, 5, 18}, {5, 9, 30}};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += max_non_overlapping_weight(b_jobs);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "interval_scheduling_weighted us=" << us << " sink=" << sink << "\n";
    return 0;
}
