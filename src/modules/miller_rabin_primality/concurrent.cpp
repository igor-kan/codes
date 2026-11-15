#include "interface.hpp"
#include <thread>
namespace codes_miller_rabin_primality {
std::vector<std::uint64_t> filter_primes_mt(const std::vector<std::uint64_t>& nums) {
    std::vector<std::uint64_t> out;
    for (std::uint64_t x : nums) if (is_prime_u64(x)) out.push_back(x);
    return out;
}
} // namespace codes_miller_rabin_primality
