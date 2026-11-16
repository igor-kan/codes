#include "interface.hpp"
#include <cassert>
#include <cstdint>

int main() {
    using namespace codes_li_chao_convex_hull_trick;
    auto t = make_lichao_tree(-500, 500);
    uint64_t rng = 0x778899AABBCCDDEEULL;
    auto nxt = [&]() -> int64_t {
        rng = rng * 6364136223846793005ULL + 1ULL;
        return static_cast<int64_t>((rng >> 32) % 201) - 100;
    };
    for (int k = 0; k < 60; ++k) {
        assert(insert_line(t, {nxt(), nxt() * 10}) == Status::Ok);
    }
    std::vector<int64_t> xs;
    for (int64_t x = -500; x <= 500; x += 5) xs.push_back(x);
    assert(verify_lichao_oracle(t, xs) == Status::Ok);
    auto bq = batch_query_min(t, xs);
    for (std::size_t i = 0; i < xs.size(); ++i) assert(bq[i] == query_min(t, xs[i]));
    return 0;
}
