#include "interface.hpp"
#include <chrono>
#include <iostream>


int main() {
    using namespace codes_ntt_number_theoretic;
    std::vector<std::uint64_t> p(64, 7), q(64, 11);
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 1000; ++iter) {
        auto r = ntt_convolve(p, q); sink += static_cast<std::int64_t>(r[iter % 64]);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "ntt_number_theoretic us=" << us << " sink=" << sink << "\n";
    return 0;
}
