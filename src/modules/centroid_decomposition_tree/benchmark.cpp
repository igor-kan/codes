#include "interface.hpp"
#include <chrono>
#include <iostream>


int main() {
    using namespace codes_centroid_decomposition_tree;
    std::vector<std::pair<int,int>> e; for(int i=1;i<127;++i) e.emplace_back((i-1)/2,i); CentroidOracle co(127,e); co.activate(0); co.activate(90);
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 1000; ++iter) {
        sink += co.nearest_active_dist(iter % 127);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "centroid_decomposition_tree us=" << us << " sink=" << sink << "\n";
    return 0;
}
