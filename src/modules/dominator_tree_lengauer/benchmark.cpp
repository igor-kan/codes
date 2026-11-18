#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_dominator_tree_lengauer;
    std::vector<std::pair<int,int>> es = {{0,1},{1,2},{1,3},{2,4},{3,4}};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        auto id = compute_immediate_dominators(5, 0, es); sink += id[4];
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "dominator_tree_lengauer us=" << us << " sink=" << sink << "\n";
    return 0;
}
