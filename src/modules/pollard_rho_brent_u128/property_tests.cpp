#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_pollard_rho_brent_u128;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    assert(is_prime_u64(2147483647ULL) && !is_prime_u64(561ULL));
    return 0;
}
