#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_lis_patience_sort_d57;
    std::vector<long long> b_xs = {0, 8, 4, 12, 2, 10, 6, 14, 1, 9};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += patience_lis_length(b_xs);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "lis_patience_sort_d57 us=" << us << " sink=" << sink << "\n";
    return 0;
}
