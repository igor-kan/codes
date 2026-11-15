#include "interface.hpp"
#include <cassert>
#include <cstdint>

int main() {
    using namespace codes_z_algorithm_lcp;
    std::uint32_t rng = 0x424242U;
    for (int t = 0; t < 25; ++t) {
        std::string s;
        for (int i = 0; i < 40 + t; ++i) {
            rng = rng * 1664525U + 1013904223U;
            s.push_back(static_cast<char>('a' + ((rng >> 28) & 3U)));
        }
        auto z1 = compute_z_array(s);
        auto z2 = compute_z_fast(s);
        assert(z1 == z2);
        assert(verify_z_invariants(s, z1) == Status::Ok);
    }
    return 0;
}
