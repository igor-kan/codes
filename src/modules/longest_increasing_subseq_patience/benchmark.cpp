#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    std::size_t sink = 0;
    std::vector<int64_t> s(1024); for(std::size_t i=0;i<1024;++i) s[i]=static_cast<int64_t>((i*37)%997);
    auto t0 = std::chrono::steady_clock::now();
    for (int it = 0; it < 200; ++it) {
        auto r = codes_longest_increasing_subseq_patience::compute_lis_patience(s); sink += r.indices.size();
    }
    auto t1 = std::chrono::steady_clock::now();
    double ns = std::chrono::duration<double, std::nano>(t1 - t0).count() / 200.0;
    std::cout << "longest_increasing_subseq_patience ns=" << ns << " sink=" << sink << "\n";
    return 0;
}
