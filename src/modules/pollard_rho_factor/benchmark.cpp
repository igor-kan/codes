#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    std::size_t sink = 0;
    (void)0;
    auto t0 = std::chrono::steady_clock::now();
    for (int it = 0; it < 200; ++it) {
        sink += codes_pollard_rho_factor::factorize_u64(1000000007ULL * 4294967291ULL % 1000000000000ULL + 15ULL).size();
    }
    auto t1 = std::chrono::steady_clock::now();
    double ns = std::chrono::duration<double, std::nano>(t1 - t0).count() / 200.0;
    std::cout << "pollard_rho_factor ns=" << ns << " sink=" << sink << "\n";
    return 0;
}
