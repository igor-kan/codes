#include "interface.hpp"
#include <cassert>
#include <cstdint>

int main() {
    using namespace codes_mo_offline_queries;
    std::vector<int> arr(120);
    std::uint32_t rng = 0x99887766U;
    for (int& v : arr) { rng = rng * 1664525U + 1013904223U; v = static_cast<int>((rng >> 24) % 15U); }
    std::vector<RangeQuery> q;
    for (std::size_t i = 0; i < 60; ++i) {
        std::size_t a = (i * 13) % 120, b = (i * 29 + 7) % 120;
        if (a > b) std::swap(a, b);
        q.push_back({a, b, i});
    }
    assert(verify_agreement(arr, q) == Status::Ok);
    return 0;
}
