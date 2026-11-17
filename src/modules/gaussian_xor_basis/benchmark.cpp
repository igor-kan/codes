#include "interface.hpp"
#include <chrono>
#include <iostream>


int main() {
    using namespace codes_gaussian_xor_basis;
    XorBasis xb; for(std::uint64_t i=1;i<=100;++i) xb.insert(i*2654435761ULL & ((1ULL<<40)-1));
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 1000; ++iter) {
        sink += static_cast<std::int64_t>(xb.max_xor(iter));
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "gaussian_xor_basis us=" << us << " sink=" << sink << "\n";
    return 0;
}
