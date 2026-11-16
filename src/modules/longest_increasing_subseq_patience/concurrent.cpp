#include "interface.hpp"
#include <algorithm>
#include <thread>

namespace codes_longest_increasing_subseq_patience {
std::vector<LisResult> batch_lis(const std::vector<std::vector<int64_t>>& seqs) {
    std::vector<LisResult> out(seqs.size());
    if (seqs.empty()) return out;
    std::size_t nt = std::min<std::size_t>(4, seqs.size());
    std::vector<std::thread> pool;
    for (std::size_t t = 0; t < nt; ++t) {
        pool.emplace_back([&, t]() {
            for (std::size_t i = t; i < seqs.size(); i += nt) {
                out[i] = compute_lis_patience(seqs[i]);
            }
        });
    }
    for (auto& th : pool) th.join();
    return out;
}
} // namespace codes_longest_increasing_subseq_patience
