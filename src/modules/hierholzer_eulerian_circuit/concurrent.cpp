#include "interface.hpp"
#include <thread>

namespace codes_hierholzer_eulerian_circuit {
std::vector<EulerResult> batch_directed_euler(const std::vector<std::pair<std::size_t, std::vector<DirectedEdge>>>& cases) {
    std::vector<EulerResult> out(cases.size());
    if (cases.empty()) return out;
    std::size_t n_threads = std::min<std::size_t>(4, cases.size());
    std::vector<std::thread> workers;
    workers.reserve(n_threads);
    for (std::size_t t = 0; t < n_threads; ++t) {
        workers.emplace_back([&, t]() {
            for (std::size_t idx = t; idx < cases.size(); idx += n_threads) {
                out[idx] = find_directed_euler_fast(cases[idx].first, cases[idx].second);
            }
        });
    }
    for (auto& w : workers) w.join();
    return out;
}
} // namespace codes_hierholzer_eulerian_circuit
