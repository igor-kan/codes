#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    std::size_t sink = 0;
    std::vector<std::vector<codes_johnson_apsp_reweight::WEdge>> g(30); for(std::size_t i=0;i<29;++i) g[i].push_back({i+1, -1.0});
    auto t0 = std::chrono::steady_clock::now();
    for (int it = 0; it < 200; ++it) {
        sink += codes_johnson_apsp_reweight::solve_johnson(30, g).dist.size();
    }
    auto t1 = std::chrono::steady_clock::now();
    double ns = std::chrono::duration<double, std::nano>(t1 - t0).count() / 200.0;
    std::cout << "johnson_apsp_reweight ns=" << ns << " sink=" << sink << "\n";
    return 0;
}
