#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_aho_corasick_dfa_d60;
    AhoCorasick ac;
    ac.add_pattern("alpha");
    ac.add_pattern("beta");
    ac.add_pattern("gamma");
    ac.build();
    std::string txt = "alphabetagammaxalphabeta";
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink = sink + ac.count_matches(txt);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "aho_corasick_dfa_d60 us=" << us << " sink=" << sink << "\n";
    return 0;
}
