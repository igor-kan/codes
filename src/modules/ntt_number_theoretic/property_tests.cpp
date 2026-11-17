#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_ntt_number_theoretic;
    std::vector<std::uint64_t> a(37), b(29);
    for (std::size_t i = 0; i < a.size(); ++i) a[i] = (i * 17 + 3) % NTT_MOD;
    for (std::size_t i = 0; i < b.size(); ++i) b[i] = (i * 31 + 5) % NTT_MOD;
    verify_ntt_exactness(a, b);
    auto batch = parallel_convolve_batch({{a, b}, {{1, 1}, {1, 2, 1}}});
    assert((batch[1] == std::vector<std::uint64_t>{1, 3, 3, 1}));
    return 0;
}
