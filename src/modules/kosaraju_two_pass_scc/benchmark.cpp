#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    std::size_t sink = 0;
    std::vector<std::vector<std::size_t>> g(500); for(std::size_t i=0;i<500;++i) g[i].push_back((i+1)%500);
    auto t0 = std::chrono::steady_clock::now();
    for (int it = 0; it < 200; ++it) {
        sink += codes_kosaraju_two_pass_scc::find_scc(500, g).num_components;
    }
    auto t1 = std::chrono::steady_clock::now();
    double ns = std::chrono::duration<double, std::nano>(t1 - t0).count() / 200.0;
    std::cout << "kosaraju_two_pass_scc ns=" << ns << " sink=" << sink << "\n";
    return 0;
}
