#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    std::size_t sink = 0;
    std::string s(4096, 'a'); s[2048] = 'b';
    auto t0 = std::chrono::steady_clock::now();
    for (int it = 0; it < 200; ++it) {
        sink += codes_z_algorithm_lcp::compute_z_fast(s)[1];
    }
    auto t1 = std::chrono::steady_clock::now();
    double ns = std::chrono::duration<double, std::nano>(t1 - t0).count() / 200.0;
    std::cout << "z_algorithm_lcp ns=" << ns << " sink=" << sink << "\n";
    return 0;
}
