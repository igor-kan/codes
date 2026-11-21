#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_dijkstra_minheap_sp;
    std::vector<std::vector<std::pair<int, long long>>> b_g(5);
    for (int i = 0; i < 4; ++i) b_g[i].push_back({i + 1, i + 2});
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += dijkstra_distances(5, 0, b_g)[4];
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "dijkstra_minheap_sp us=" << us << " sink=" << sink << "\n";
    return 0;
}
