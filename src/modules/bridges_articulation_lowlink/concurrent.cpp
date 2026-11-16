#include "interface.hpp"
#include <algorithm>
#include <thread>

namespace codes_bridges_articulation_lowlink {
std::vector<CutReport> batch_cut_reports(const std::vector<std::pair<std::size_t, std::vector<UndirectedEdge>>>& graphs) {
    std::vector<CutReport> out(graphs.size());
    if (graphs.empty()) return out;
    std::size_t nt = std::min<std::size_t>(4, graphs.size());
    std::vector<std::thread> pool;
    for (std::size_t t = 0; t < nt; ++t) {
        pool.emplace_back([&, t]() {
            for (std::size_t i = t; i < graphs.size(); i += nt) {
                out[i] = find_bridges_iterative(graphs[i].first, graphs[i].second);
            }
        });
    }
    for (auto& th : pool) th.join();
    return out;
}
} // namespace codes_bridges_articulation_lowlink
