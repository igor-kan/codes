#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    std::size_t sink = 0;
    std::vector<codes_bridges_articulation_lowlink::UndirectedEdge> e; for(std::size_t i=0;i<64;++i){e.push_back({i,(i+1)%64}); if(i%4==0) e.push_back({i,(i+3)%64});}
    auto t0 = std::chrono::steady_clock::now();
    for (int it = 0; it < 200; ++it) {
        auto r = codes_bridges_articulation_lowlink::find_bridges_iterative(64, e); sink += r.bridge_edge_ids.size() + r.articulation_vertices.size();
    }
    auto t1 = std::chrono::steady_clock::now();
    double ns = std::chrono::duration<double, std::nano>(t1 - t0).count() / 200.0;
    std::cout << "bridges_articulation_lowlink ns=" << ns << " sink=" << sink << "\n";
    return 0;
}
