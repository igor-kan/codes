#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_link_cut_tree_splay {
class LinkCutTree {
public:
    explicit LinkCutTree(int n);
    void set_value(int u, std::int64_t val);
    void make_root(int u);
    int find_root(int u);
    bool connected(int u, int v);
    bool link(int u, int v);
    bool cut(int u, int v);
    std::int64_t query_path_sum(int u, int v);
    std::int64_t query_path_max(int u, int v);
    int size() const { return static_cast<int>(nodes_.size()); }
    const std::vector<LctNode>& raw_nodes() const { return nodes_; }

private:
    std::vector<LctNode> nodes_;
    bool is_root(int x) const;
    void push(int x);
    void pull(int x);
    void rotate(int x);
    void splay(int x);
    void access(int x);
};

void validate_vertex(int n, int v);
std::vector<bool> fast_connectivity_batch(LinkCutTree& lct, const std::vector<std::pair<int, int>>& pairs);
std::vector<std::int64_t> parallel_forest_path_sums(int n, const std::vector<std::pair<int, int>>& edges,
                                                    const std::vector<std::int64_t>& weights,
                                                    const std::vector<std::pair<int, int>>& queries);
void verify_lct_invariants(const LinkCutTree& lct);
} // namespace codes_link_cut_tree_splay
