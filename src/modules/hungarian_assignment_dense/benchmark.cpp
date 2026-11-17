#include "interface.hpp"
#include <chrono>
#include <iostream>


int main() {
    using namespace codes_hungarian_assignment_dense;
    std::vector<std::vector<std::int64_t>> c(12, std::vector<std::int64_t>(12, 0)); for(int i=0;i<12;++i) for(int j=0;j<12;++j) c[i][j]=(i*7+j*11)%29;
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 1000; ++iter) {
        sink += solve_min_assignment(c).total_cost;
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "hungarian_assignment_dense us=" << us << " sink=" << sink << "\n";
    return 0;
}
