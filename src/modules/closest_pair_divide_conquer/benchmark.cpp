#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    std::size_t sink = 0;
    std::vector<codes_closest_pair_divide_conquer::Point2D> p; for(std::size_t i=0;i<256;++i) p.push_back({double((i*37)%251), double((i*53)%257), i});
    auto t0 = std::chrono::steady_clock::now();
    for (int it = 0; it < 200; ++it) {
        auto r = codes_closest_pair_divide_conquer::closest_pair_dc(p); sink += r.i;
    }
    auto t1 = std::chrono::steady_clock::now();
    double ns = std::chrono::duration<double, std::nano>(t1 - t0).count() / 200.0;
    std::cout << "closest_pair_divide_conquer ns=" << ns << " sink=" << sink << "\n";
    return 0;
}
