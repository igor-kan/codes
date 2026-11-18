#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_persistent_treap_split;
    PersistentTreap pt; int r = -1; for (int i = 0; i < 16; ++i) r = pt.merge(r, pt.new_node(i, i * 17u + 1u));
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += pt.range_sum(r, 2, 10);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "persistent_treap_split us=" << us << " sink=" << sink << "\n";
    return 0;
}
