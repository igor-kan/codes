#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_heavy_light_lca_d58 {
class BinaryLiftLca {
public:
    BinaryLiftLca(int n, int root, const std::vector<std::pair<int, int>>& edges);
    int lca(int u, int v) const;
    int dist(int u, int v) const;
private:
    int n_;
    int lg_;
    std::vector<int> depth_;
    std::vector<std::vector<int>> up_;
};

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_heavy_light_lca_d58
