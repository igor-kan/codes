#include "interface.hpp"
#include <thread>

namespace codes_gaussian_xor_basis {
std::vector<std::uint64_t> parallel_basis_max_queries(
    const std::vector<std::uint64_t>& nums,
    const std::vector<std::uint64_t>& seeds
) {
    XorBasis b;
    for (auto v : nums) b.insert(v);
    std::vector<std::uint64_t> out(seeds.size(), 0);
    std::size_t mid = seeds.size() / 2;
    auto run = [&](std::size_t lo, std::size_t hi) {
        for (std::size_t i = lo; i < hi; ++i) out[i] = b.max_xor(seeds[i]);
    };
    std::thread t1(run, 0, mid);
    std::thread t2(run, mid, seeds.size());
    t1.join();
    t2.join();
    return out;
}
} // namespace codes_gaussian_xor_basis
