#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_sliding_window_deque_extrema;
    std::vector<long long> b_xs = {9, 4, 7, 1, 8, 3, 5, 2};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += sliding_window_max(b_xs, 4).back();
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "sliding_window_deque_extrema us=" << us << " sink=" << sink << "\n";
    return 0;
}
