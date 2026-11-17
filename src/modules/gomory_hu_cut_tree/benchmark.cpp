#include "interface.hpp"
#include <chrono>
#include <iostream>


int main() {
    using namespace codes_gomory_hu_cut_tree;
    std::vector<UndirectedEdge> e={{0,1,4},{1,2,3},{2,3,5},{0,3,2},{1,3,6}};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 1000; ++iter) {
        auto t=build_gomory_hu_tree(4,e); sink += query_pair_min_cut(4, t, 0, 3);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "gomory_hu_cut_tree us=" << us << " sink=" << sink << "\n";
    return 0;
}
