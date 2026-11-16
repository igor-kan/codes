#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_li_chao_convex_hull_trick {
LiChaoTree make_lichao_tree(int64_t lo, int64_t hi);
Status insert_line(LiChaoTree& tree, LineFn fn);
int64_t query_min(const LiChaoTree& tree, int64_t x);
int64_t query_min_fast(const LiChaoTree& tree, int64_t x);
std::vector<int64_t> batch_query_min(const LiChaoTree& tree, const std::vector<int64_t>& xs);
Status verify_lichao_oracle(const LiChaoTree& tree, const std::vector<int64_t>& xs);
} // namespace codes_li_chao_convex_hull_trick
