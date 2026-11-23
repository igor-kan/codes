#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_rolling_median_multiset_d58;
    std::vector<long long> bxs = {4, 1, 9, 2, 7, 5, 8, 3};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += sliding_window_medians(bxs, 5).back();
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "rolling_median_multiset_d58 us=" << us << " sink=" << sink << "\n";
    return 0;
}
