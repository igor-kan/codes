#include "interface.hpp"
#include <chrono>
#include <iostream>


int main() {
    using namespace codes_pairing_heap_meldable;
    std::vector<std::int64_t> data(128); for(int i=0;i<128;++i) data[i]=(i*43)%128;
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 1000; ++iter) {
        auto out = fast_heapsort_pairing(data); sink += out[iter % 128];
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "pairing_heap_meldable us=" << us << " sink=" << sink << "\n";
    return 0;
}
