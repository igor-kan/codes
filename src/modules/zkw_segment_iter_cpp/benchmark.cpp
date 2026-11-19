#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_zkw_segment_iter_cpp;
    ZkwSegTree st(16); for (int i = 0; i < 16; ++i) st.point_set(i, i + 1);
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += st.range_sum(2, 12);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "zkw_segment_iter_cpp us=" << us << " sink=" << sink << "\n";
    return 0;
}
