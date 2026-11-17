#include "interface.hpp"
#include <chrono>
#include <iostream>


int main() {
    using namespace codes_blossom_general_matching;
    std::vector<std::pair<int,int>> g; for(int i=0;i<11;++i) g.emplace_back(i,(i+1)%11); g.emplace_back(0,5);
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 1000; ++iter) {
        sink += edmonds_blossom_matching(11, g).pairs;
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "blossom_general_matching us=" << us << " sink=" << sink << "\n";
    return 0;
}
