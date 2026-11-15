#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    std::size_t sink = 0;
    (void)0;
    auto t0 = std::chrono::steady_clock::now();
    for (int it = 0; it < 200; ++it) {
        if (codes_miller_rabin_primality::is_prime_u64(1000000007ULL + it)) sink++;
    }
    auto t1 = std::chrono::steady_clock::now();
    double ns = std::chrono::duration<double, std::nano>(t1 - t0).count() / 200.0;
    std::cout << "miller_rabin_primality ns=" << ns << " sink=" << sink << "\n";
    return 0;
}
