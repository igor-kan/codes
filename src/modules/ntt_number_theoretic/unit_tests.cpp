#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_ntt_number_theoretic;
    auto c = ntt_convolve({1, 2, 3}, {4, 5, 6});
    assert((c == std::vector<std::uint64_t>{4, 13, 28, 27, 18}));
    verify_ntt_exactness({10, 20, 30, 40}, {7, 8, 9});
    return 0;
}
