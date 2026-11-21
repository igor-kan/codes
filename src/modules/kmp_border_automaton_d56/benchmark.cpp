#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_kmp_border_automaton_d56;
    std::string b_txt = "abcabcdabxabcdabcdabde";
    std::string b_pat = "abcdabd";
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += static_cast<long long>(kmp_find_all(b_txt, b_pat).size());
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "kmp_border_automaton_d56 us=" << us << " sink=" << sink << "\n";
    return 0;
}
