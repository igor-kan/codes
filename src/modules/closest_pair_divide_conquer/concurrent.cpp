#include "interface.hpp"
#include <algorithm>
#include <thread>

namespace codes_closest_pair_divide_conquer {
std::vector<PairResult> batch_closest_pairs(const std::vector<std::vector<Point2D>>& clouds) {
    std::vector<PairResult> out(clouds.size());
    if (clouds.empty()) return out;
    std::size_t nt = std::min<std::size_t>(4, clouds.size());
    std::vector<std::thread> pool;
    for (std::size_t t = 0; t < nt; ++t) {
        pool.emplace_back([&, t]() {
            for (std::size_t i = t; i < clouds.size(); i += nt) {
                out[i] = closest_pair_dc(clouds[i]);
            }
        });
    }
    for (auto& th : pool) th.join();
    return out;
}
} // namespace codes_closest_pair_divide_conquer
