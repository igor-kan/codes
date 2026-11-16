#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_li_chao_convex_hull_trick {
struct LineFn {
    int64_t m = 0;
    int64_t c = 0;
    int64_t eval(int64_t x) const { return m * x + c; }
};

struct LiChaoNode {
    LineFn fn;
    int left = -1;
    int right = -1;
    bool has_fn = false;
};

struct LiChaoTree {
    int64_t x_lo = -100000;
    int64_t x_hi = 100000;
    std::vector<LiChaoNode> nodes;
    std::vector<LineFn> inserted;
};
} // namespace codes_li_chao_convex_hull_trick
