#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_cartesian_tree_rmq_lca {
class CartesianTree {
public:
    explicit CartesianTree(const std::vector<std::int64_t>& arr);
    int root() const { return root_; }
    int rmq_index(int l, int r) const;
    const std::vector<CartesianNode>& nodes() const { return nodes_; }
private:
    int root_ = -1;
    std::vector<CartesianNode> nodes_;
};

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_cartesian_tree_rmq_lca
