#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_li_chao_segment_d60;
    LiChaoTree lc(0, 255);
    lc.add_line(3, 5);
    lc.add_line(-2, 400);
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        lc.add_line(1, iter % 17);
    sink = sink + lc.min_at(iter & 255);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "li_chao_segment_d60 us=" << us << " sink=" << sink << "\n";
    return 0;
}
