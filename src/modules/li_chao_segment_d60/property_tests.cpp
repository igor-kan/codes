#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_li_chao_segment_d60;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    LiChaoTree lc(0, 100);
    std::vector<std::pair<std::int64_t, std::int64_t>> lines = {{3, 1}, {-2, 150}, {1, 40}, {0, 75}};
    for (auto [m, b] : lines) lc.add_line(m, b);
    for (int x = 0; x <= 100; ++x) {
        std::int64_t brute = lines[0].first * x + lines[0].second;
        for (auto [m, b] : lines) brute = std::min(brute, m * x + b);
        assert(lc.min_at(x) == brute);
    }
    return 0;
}
