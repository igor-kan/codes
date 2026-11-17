#include "interface.hpp"
#include <chrono>
#include <iostream>


int main() {
    using namespace codes_two_sat_implication;
    TwoSatSolver solver(40); for(int i=0;i<39;++i) solver.add_xor(i, i+1);
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 1000; ++iter) {
        auto r = solver.solve(); sink += r.satisfiable ? static_cast<int>(r.assignment.size()) : 0;
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "two_sat_implication us=" << us << " sink=" << sink << "\n";
    return 0;
}
