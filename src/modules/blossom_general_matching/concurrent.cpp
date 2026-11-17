#include "interface.hpp"
#include <thread>

namespace codes_blossom_general_matching {
std::vector<MatchingResult> parallel_matching_batch(
    const std::vector<std::pair<int, std::vector<std::pair<int, int>>>>& graphs
) {
    std::vector<MatchingResult> out(graphs.size());
    std::size_t mid = graphs.size() / 2;
    auto worker = [&](std::size_t lo, std::size_t hi) {
        for (std::size_t i = lo; i < hi; ++i) {
            out[i] = edmonds_blossom_matching(graphs[i].first, graphs[i].second);
        }
    };
    std::thread t1(worker, 0, mid);
    std::thread t2(worker, mid, graphs.size());
    t1.join();
    t2.join();
    return out;
}
} // namespace codes_blossom_general_matching
