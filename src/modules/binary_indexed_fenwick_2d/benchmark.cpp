#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_binary_indexed_fenwick_2d;
    Fenwick2D b_fw(8, 8);
    for (int i = 0; i < 8; ++i) b_fw.add(i, i, 3);
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += b_fw.rect_sum(0, 0, 7, 7);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "binary_indexed_fenwick_2d us=" << us << " sink=" << sink << "\n";
    return 0;
}
