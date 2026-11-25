#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_li_chao_segment_d60 {
class LiChaoTree {
    int lo_, hi_;
    std::vector<LinearFn> tree_;
    void insert_rec(int node, int l, int r, LinearFn fn);
    std::int64_t query_rec(int node, int l, int r, int x) const;
public:
    LiChaoTree(int lo, int hi);
    void add_line(std::int64_t m, std::int64_t b);
    std::int64_t min_at(int x) const;
};

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_li_chao_segment_d60
