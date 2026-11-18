#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_directed_mst_chu_liu;
    std::vector<DirEdge> es = {{0,1,10},{0,2,20},{1,2,2},{2,1,3},{2,3,4}};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += edmonds_directed_mst(4, 0, es);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "directed_mst_chu_liu us=" << us << " sink=" << sink << "\n";
    return 0;
}
