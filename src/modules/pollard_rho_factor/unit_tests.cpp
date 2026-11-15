#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_pollard_rho_factor;
    auto f1 = factorize_u64(60);
    assert((f1 == std::vector<std::uint64_t>{2, 2, 3, 5}));
    // Semiprime 1000000007 * 1000000009
    std::uint64_t semi = 1000000007ULL * 1000000009ULL;
    auto f2 = factorize_u64(semi);
    assert((f2 == std::vector<std::uint64_t>{1000000007ULL, 1000000009ULL}));
    assert(verify_factorization(semi, f2) == Status::Ok);
    return 0;
}
