#include "interface.hpp"
#include <algorithm>
#include <thread>
#include <tuple>

namespace codes_min_cost_max_flow_spfa {
std::vector<FlowSolution> batch_mcmf(const std::vector<std::tuple<std::size_t, std::size_t, std::size_t, std::vector<FlowArc>>>& tasks) {
    std::vector<FlowSolution> out(tasks.size());
    if (tasks.empty()) return out;
    std::size_t nt = std::min<std::size_t>(4, tasks.size());
    std::vector<std::thread> pool;
    for (std::size_t t = 0; t < nt; ++t) {
        pool.emplace_back([&, t]() {
            for (std::size_t i = t; i < tasks.size(); i += nt) {
                const auto& [n, s, d, arcs] = tasks[i];
                out[i] = solve_mcmf_potentials(n, s, d, arcs);
            }
        });
    }
    for (auto& th : pool) th.join();
    return out;
}
} // namespace codes_min_cost_max_flow_spfa
