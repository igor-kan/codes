#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_dinic_max_flow_d60;
    std::int64_t total_f = 0;
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        DinicFlow df(4);
    df.add_edge(0, 1, 3 + (iter & 7)); df.add_edge(1, 3, 4);
    df.add_edge(0, 2, 5); df.add_edge(2, 3, 2 + (iter & 3));
    total_f = df.max_flow(0, 3);
    sink = sink + total_f;
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "dinic_max_flow_d60 us=" << us << " sink=" << sink << "\n";
    return 0;
}
