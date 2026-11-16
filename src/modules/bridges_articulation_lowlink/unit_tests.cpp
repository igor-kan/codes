#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_bridges_articulation_lowlink;
    std::vector<UndirectedEdge> g = {{0,1},{1,2},{2,0},{1,3},{3,4},{4,5},{5,3},{2,6},{2,6}};
    auto r = find_bridges_and_articulations(7, g);
    auto r2 = find_bridges_iterative(7, g);
    assert(r.bridge_edge_ids == r2.bridge_edge_ids);
    assert(r.articulation_vertices == r2.articulation_vertices);
    assert(r.bridge_edge_ids.size() == 1 && r.bridge_edge_ids[0] == 3);
    assert(verify_cut_oracle(7, g, r) == Status::Ok);
    return 0;
}
