#include "interface.hpp"
#include <thread>

namespace codes_bellman_ford_spfa {
std::vector<SsspResult> batch_sources(std::size_t n, const std::vector<std::vector<Edge>>& adj, const std::vector<std::size_t>& srcs) {
    std::vector<SsspResult> out(srcs.size());
    std::vector<std::thread> th;
    for (std::size_t i = 0; i < srcs.size(); ++i) {
        th.emplace_back([&, i]() { out[i] = solve_spfa_slf(n, adj, srcs[i]); });
    }
    for (auto& t : th) t.join();
    return out;
}
} // namespace codes_bellman_ford_spfa
