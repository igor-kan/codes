#include "interface.hpp"
#include <cassert>
#include <cstdint>

int main() {
    using namespace codes_longest_increasing_subseq_patience;
    uint64_t s = 0x13579BDF02468ACEULL;
    auto nxt = [&]() -> int64_t { s ^= s << 13; s ^= s >> 7; s ^= s << 17; return static_cast<int64_t>(s % 100) - 50; };
    std::vector<std::vector<int64_t>> seqs;
    for (int k = 0; k < 20; ++k) {
        std::vector<int64_t> v(45);
        for (auto& x : v) x = nxt();
        seqs.push_back(std::move(v));
    }
    auto res = batch_lis(seqs);
    for (std::size_t i = 0; i < seqs.size(); ++i) {
        assert(res[i].indices.size() == compute_lis_length_fast(seqs[i]));
        assert(verify_lis_invariants(seqs[i], res[i]) == Status::Ok);
    }
    return 0;
}
