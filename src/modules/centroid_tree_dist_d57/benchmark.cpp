#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_centroid_tree_dist_d57;
    std::vector<std::pair<int, int>> b_tr = {{0,1},{1,2},{1,3},{3,4},{4,5}};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += compute_tree_extent(6, b_tr).diameter;
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "centroid_tree_dist_d57 us=" << us << " sink=" << sink << "\n";
    return 0;
}
