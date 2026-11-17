#include "interface.hpp"
#include <thread>

namespace codes_ntt_number_theoretic {
std::vector<std::vector<std::uint64_t>> parallel_convolve_batch(
    const std::vector<std::pair<std::vector<std::uint64_t>, std::vector<std::uint64_t>>>& pairs
) {
    std::vector<std::vector<std::uint64_t>> out(pairs.size());
    std::size_t mid = pairs.size() / 2;
    auto run = [&](std::size_t lo, std::size_t hi) {
        for (std::size_t i = lo; i < hi; ++i) {
            out[i] = ntt_convolve(pairs[i].first, pairs[i].second);
        }
    };
    std::thread t1(run, 0, mid);
    std::thread t2(run, mid, pairs.size());
    t1.join();
    t2.join();
    return out;
}
} // namespace codes_ntt_number_theoretic
