#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_pollard_rho_brent_u128;
    validate_problem_size(1);
    auto fs = factorize_u64(360360ULL);
    std::uint64_t prod = 1;
    for (auto p : fs) { assert(is_prime_u64(p)); prod *= p; }
    assert(prod == 360360ULL);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
