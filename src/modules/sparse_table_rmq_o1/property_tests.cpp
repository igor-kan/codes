#include "interface.hpp"
#include <cassert>
#include <cstdint>

int main() {
    using namespace codes_sparse_table_rmq_o1;
    uint64_t s = 0x5555AAAA11119999ULL;
    std::vector<int64_t> a(80);
    for (auto& x : a) {
        s = s * 6364136223846793005ULL + 1ULL;
        x = static_cast<int64_t>(s % 2000) - 1000;
    }
    auto tab = build_sparse_table(a);
    assert(verify_table_invariants(tab, a) == Status::Ok);
    std::vector<std::pair<std::size_t, std::size_t>> qs;
    for (std::size_t i = 0; i < a.size(); ++i) qs.push_back({0, i});
    auto res = batch_query_rmq(tab, qs);
    for (std::size_t i = 0; i < qs.size(); ++i) {
        assert(res[i] == query_rmq_o1(tab, qs[i].first, qs[i].second));
    }
    return 0;
}
