#include "interface.hpp"
namespace codes_miller_rabin_primality {
Status verify_primality_agreement(std::uint64_t limit) {
    for (std::uint64_t x = 0; x <= limit; ++x) {
        if (is_prime_u64(x) != is_prime_trial(x)) return Status::InvariantViolation;
    }
    return Status::Ok;
}
} // namespace codes_miller_rabin_primality
