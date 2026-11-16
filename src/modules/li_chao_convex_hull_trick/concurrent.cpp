#include "interface.hpp"
#include <algorithm>
#include <thread>

namespace codes_li_chao_convex_hull_trick {
std::vector<int64_t> batch_query_min(const LiChaoTree& tree, const std::vector<int64_t>& xs) {
    std::vector<int64_t> out(xs.size(), 0);
    if (xs.empty()) return out;
    std::size_t nt = std::min<std::size_t>(4, xs.size());
    std::vector<std::thread> pool;
    for (std::size_t t = 0; t < nt; ++t) {
        pool.emplace_back([&, t]() {
            for (std::size_t i = t; i < xs.size(); i += nt) {
                out[i] = query_min_fast(tree, xs[i]);
            }
        });
    }
    for (auto& th : pool) th.join();
    return out;
}
} // namespace codes_li_chao_convex_hull_trick
