#include "interface.hpp"
#include <thread>

namespace codes_dominator_tree_lengauer {

std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches) {
    std::vector<std::int64_t> out(batches.size(), 0);
    std::size_t mid = batches.size() / 2;
    auto worker = [&](std::size_t lo, std::size_t hi) {
        for (std::size_t i = lo; i < hi; ++i) {
            out[i] = fast_checksum_span(batches[i]);
        }
    };
    std::thread t1(worker, 0, mid);
    std::thread t2(worker, mid, batches.size());
    t1.join();
    t2.join();
    return out;
}

} // namespace codes_dominator_tree_lengauer
