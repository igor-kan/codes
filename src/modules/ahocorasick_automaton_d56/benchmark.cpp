#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_ahocorasick_automaton_d56;
    std::vector<std::string> b_pats = {"alpha", "beta", "al"};
    std::string b_txt = "alphabetabetal";
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += ac_count_matches(b_pats, b_txt);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "ahocorasick_automaton_d56 us=" << us << " sink=" << sink << "\n";
    return 0;
}
