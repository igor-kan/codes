#include "interface.hpp"
namespace codes_pollard_rho_factor {
std::vector<FactorReport> batch_factorize(const std::vector<std::uint64_t>& nums) {
    std::vector<FactorReport> reps;
    reps.reserve(nums.size());
    for (auto n : nums) reps.push_back({n, factorize_u64(n)});
    return reps;
}
} // namespace codes_pollard_rho_factor
