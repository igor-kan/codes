#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_pollard_rho_factor;
    for (std::uint64_t n = 2; n <= 500; n += 13) {
        auto f = factorize_u64(n);
        assert(verify_factorization(n, f) == Status::Ok);
    }
    return 0;
}
