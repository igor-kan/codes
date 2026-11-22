#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_rabin_karp_rolling_d57;
    std::string bt = "pattern_matching_pattern_test", bp = "pattern";
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += static_cast<long long>(rabin_karp_search(bt, bp).size());
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "rabin_karp_rolling_d57 us=" << us << " sink=" << sink << "\n";
    return 0;
}
