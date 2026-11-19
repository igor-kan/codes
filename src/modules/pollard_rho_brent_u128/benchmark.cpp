#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_pollard_rho_brent_u128;
    std::uint64_t n = 10403ULL;
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += static_cast<std::int64_t>(factorize_u64(n).size());
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "pollard_rho_brent_u128 us=" << us << " sink=" << sink << "\n";
    return 0;
}
