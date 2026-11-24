#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_mos_distinct_freq_d59;
    std::vector<int> bxs = {1, 1, 2, 1, 2, 2};
    std::vector<std::pair<int, int>> bqs = {{0, 5}, {1, 4}};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += count_equal_pairs_queries(bxs, bqs)[0];
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "mos_distinct_freq_d59 us=" << us << " sink=" << sink << "\n";
    return 0;
}
