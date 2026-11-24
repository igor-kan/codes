#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_euler_tour_subtree_d59;
    std::vector<long long> bw = {1,2,3,4};
    std::vector<std::pair<int, int>> be = {{0,1},{0,2},{2,3}};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += all_subtree_sums(4, 0, bw, be)[0];
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "euler_tour_subtree_d59 us=" << us << " sink=" << sink << "\n";
    return 0;
}
