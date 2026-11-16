#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    std::size_t sink = 0;
    std::vector<codes_min_cost_max_flow_spfa::FlowArc> a; for(std::size_t i=0;i<15;++i){a.push_back({i,i+1,5,2}); a.push_back({i,(i+2)%16,3,5});}
    auto t0 = std::chrono::steady_clock::now();
    for (int it = 0; it < 200; ++it) {
        auto r = codes_min_cost_max_flow_spfa::solve_mcmf_potentials(16, 0, 15, a); sink += static_cast<std::size_t>(r.total_cost);
    }
    auto t1 = std::chrono::steady_clock::now();
    double ns = std::chrono::duration<double, std::nano>(t1 - t0).count() / 200.0;
    std::cout << "min_cost_max_flow_spfa ns=" << ns << " sink=" << sink << "\n";
    return 0;
}
