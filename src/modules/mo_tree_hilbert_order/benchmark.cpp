#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_mo_tree_hilbert_order;
    std::vector<int> a = {1,2,1,3,2,4}; std::vector<std::pair<int,int>> qs = {{0,3},{2,5}};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += mo_distinct_queries(a, qs)[0];
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "mo_tree_hilbert_order us=" << us << " sink=" << sink << "\n";
    return 0;
}
