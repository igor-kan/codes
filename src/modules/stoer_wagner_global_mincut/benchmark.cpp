#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_stoer_wagner_global_mincut;
    std::vector<std::vector<std::int64_t>> g = {{0,3,1},{3,0,2},{1,2,0}};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += stoer_wagner_mincut(3, g).weight;
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "stoer_wagner_global_mincut us=" << us << " sink=" << sink << "\n";
    return 0;
}
