#include "interface.hpp"
#include <cassert>
#include <cstdint>
#include <tuple>

int main() {
    using namespace codes_min_cost_max_flow_spfa;
    uint64_t s = 0x987654321ULL;
    auto rnd = [&]() -> int64_t { s = s * 1103515245ULL + 12345ULL; return static_cast<int64_t>((s >> 16) & 0x7FFF); };
    std::vector<std::tuple<std::size_t, std::size_t, std::size_t, std::vector<FlowArc>>> tasks;
    for (int k = 0; k < 12; ++k) {
        std::size_t n = 6 + (k % 4);
        std::vector<FlowArc> arcs;
        for (int e = 0; e < 18; ++e) {
            std::size_t u = static_cast<std::size_t>(rnd()) % n;
            std::size_t v = static_cast<std::size_t>(rnd()) % n;
            if (u != v) arcs.push_back({u, v, 1 + (rnd() % 10), 1 + (rnd() % 20)});
        }
        tasks.emplace_back(n, 0, n - 1, std::move(arcs));
    }
    auto res = batch_mcmf(tasks);
    for (std::size_t i = 0; i < tasks.size(); ++i) {
        const auto& [n, src, dst, arcs] = tasks[i];
        auto r0 = solve_mcmf_spfa(n, src, dst, arcs);
        assert(res[i].total_flow == r0.total_flow);
        assert(res[i].total_cost == r0.total_cost);
        assert(verify_flow_invariants(n, src, dst, arcs, res[i]) == Status::Ok);
    }
    return 0;
}
