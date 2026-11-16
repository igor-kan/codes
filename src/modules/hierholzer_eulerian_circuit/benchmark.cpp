#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    std::size_t sink = 0;
    std::vector<codes_hierholzer_eulerian_circuit::DirectedEdge> e; for(std::size_t i=0;i<256;++i) e.push_back({i%32,(i+1)%32});
    auto t0 = std::chrono::steady_clock::now();
    for (int it = 0; it < 200; ++it) {
        auto r = codes_hierholzer_eulerian_circuit::find_directed_euler_fast(32, e); sink += r.vertices.size();
    }
    auto t1 = std::chrono::steady_clock::now();
    double ns = std::chrono::duration<double, std::nano>(t1 - t0).count() / 200.0;
    std::cout << "hierholzer_eulerian_circuit ns=" << ns << " sink=" << sink << "\n";
    return 0;
}
