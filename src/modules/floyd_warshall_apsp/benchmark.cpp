#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    std::size_t sink = 0;
    std::vector<double> w(32*32, 5.0); for(int i=0;i<32;++i) w[i*32+i]=0.0;
    auto t0 = std::chrono::steady_clock::now();
    for (int it = 0; it < 200; ++it) {
        sink += codes_floyd_warshall_apsp::solve_apsp_blocked(32, w).dist.size();
    }
    auto t1 = std::chrono::steady_clock::now();
    double ns = std::chrono::duration<double, std::nano>(t1 - t0).count() / 200.0;
    std::cout << "floyd_warshall_apsp ns=" << ns << " sink=" << sink << "\n";
    return 0;
}
