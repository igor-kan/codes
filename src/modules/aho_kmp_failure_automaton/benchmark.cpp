#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_aho_kmp_failure_automaton;
    std::vector<std::string> ps = {"ab", "aba", "ba"};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += scan_ac_dfa(ps, "abababa").matches;
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "aho_kmp_failure_automaton us=" << us << " sink=" << sink << "\n";
    return 0;
}
