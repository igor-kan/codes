#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_hierholzer_eulerian_circuit;
    std::vector<DirectedEdge> cyc = {{0,1},{1,2},{2,0},{1,3},{3,1}};
    auto r1 = find_directed_euler(4, cyc);
    assert(r1.valid);
    assert(verify_euler_invariants(4, cyc, r1) == Status::Ok);
    assert(r1.vertices.front() == r1.vertices.back());

    std::vector<DirectedEdge> trail = {{0,1},{1,2},{2,0},{0,3}};
    auto r2 = find_directed_euler_fast(4, trail);
    assert(r2.valid);
    assert(verify_euler_invariants(4, trail, r2) == Status::Ok);
    assert(r2.vertices.front() == 0 && r2.vertices.back() == 3);

    std::vector<DirectedEdge> bad = {{0,1},{1,2},{3,4},{4,3}};
    assert(!find_directed_euler(5, bad).valid);
    return 0;
}
