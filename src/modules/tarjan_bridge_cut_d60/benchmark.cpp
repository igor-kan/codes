#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_tarjan_bridge_cut_d60;
    std::vector<GraphEdge> es = {{0,1},{1,2},{2,3},{3,4},{4,2},{4,5}};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        auto r = find_bridges_and_cuts(6, es);
    sink = sink + static_cast<std::int64_t>(r.bridges.size() + r.cut_vertices.size());
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "tarjan_bridge_cut_d60 us=" << us << " sink=" << sink << "\n";
    return 0;
}
