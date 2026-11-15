#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    std::size_t sink = 0;
    std::vector<std::vector<codes_bellman_ford_spfa::Edge>> g(200); for(int i=0;i<199;++i) g[i].push_back({(std::size_t)i+1, 1.0});
    auto t0 = std::chrono::steady_clock::now();
    for (int it = 0; it < 200; ++it) {
        sink += codes_bellman_ford_spfa::solve_spfa_slf(200, g, 0).dist.size();
    }
    auto t1 = std::chrono::steady_clock::now();
    double ns = std::chrono::duration<double, std::nano>(t1 - t0).count() / 200.0;
    std::cout << "bellman_ford_spfa ns=" << ns << " sink=" << sink << "\n";
    return 0;
}
