#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_trie_xor_query_d59;
    XorTrie b_tr; for (unsigned x = 1; x <= 16; ++x) b_tr.insert(x * 7u);
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += b_tr.max_xor(13u);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "trie_xor_query_d59 us=" << us << " sink=" << sink << "\n";
    return 0;
}
