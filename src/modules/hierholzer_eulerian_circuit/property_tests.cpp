#include "interface.hpp"
#include <cassert>
#include <cstdint>

int main() {
    using namespace codes_hierholzer_eulerian_circuit;
    uint64_t rng = 0x123456789ABCDEF0ULL;
    auto next_u64 = [&]() -> uint64_t {
        rng ^= rng >> 12;
        rng ^= rng << 25;
        rng ^= rng >> 27;
        return rng * 0x2545F4914F6CDD1DULL;
    };
    std::vector<std::pair<std::size_t, std::vector<DirectedEdge>>> cases;
    for (int c = 0; c < 12; ++c) {
        std::size_t n = 6 + (c % 5);
        std::size_t m = 24 + c * 3;
        std::vector<DirectedEdge> e;
        std::size_t cur = 0;
        for (std::size_t k = 0; k < m; ++k) {
            std::size_t nxt = (k + 1 == m) ? 0 : static_cast<std::size_t>(next_u64() % n);
            e.push_back({cur, nxt});
            cur = nxt;
        }
        cases.push_back({n, e});
    }
    auto res = batch_directed_euler(cases);
    for (std::size_t i = 0; i < cases.size(); ++i) {
        auto r0 = find_directed_euler(cases[i].first, cases[i].second);
        assert(res[i].valid && r0.valid);
        assert(verify_euler_invariants(cases[i].first, cases[i].second, res[i]) == Status::Ok);
        assert(verify_euler_invariants(cases[i].first, cases[i].second, r0) == Status::Ok);
    }
    return 0;
}
