#include "interface.hpp"
#include <chrono>
#include <iostream>


int main() {
    using namespace codes_link_cut_tree_splay;
    LinkCutTree lct(64); for(int i=0;i<64;++i) lct.set_value(i, i+1); for(int i=0;i<63;++i) lct.link(i, i+1);
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 1000; ++iter) {
        sink += lct.query_path_sum(iter % 17, 40 + (iter % 23));
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "link_cut_tree_splay us=" << us << " sink=" << sink << "\n";
    return 0;
}
