#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_cartesian_tree_rmq_lca;
    std::vector<std::int64_t> a = {9, 3, 7, 1, 8, 12, 10, 5}; CartesianTree ct(a);
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += ct.rmq_index(0, 6);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "cartesian_tree_rmq_lca us=" << us << " sink=" << sink << "\n";
    return 0;
}
