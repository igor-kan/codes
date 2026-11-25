#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_sparse_table_rmq_d60;
    std::vector<std::int64_t> a(128);
    for (int i = 0; i < 128; ++i) a[i] = (i * 37) % 101;
    SparseTableRmq st(a);
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        int l = iter & 63, r = l + 32;
    sink = sink + st.query(l, r);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "sparse_table_rmq_d60 us=" << us << " sink=" << sink << "\n";
    return 0;
}
