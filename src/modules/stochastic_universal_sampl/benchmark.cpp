#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_stochastic_universal_sampl;
    std::vector<double> w = {1.0, 3.0, 6.0, 10.0}; VoseAliasSampler vs(w);
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += vs.sample_one(iter % 4, 0.35);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "stochastic_universal_sampl us=" << us << " sink=" << sink << "\n";
    return 0;
}
