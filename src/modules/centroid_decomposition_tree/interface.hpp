#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_centroid_decomposition_tree {
class CentroidOracle {
public:
    explicit CentroidOracle(int n, const std::vector<std::pair<int, int>>& edges);
    void activate(int u);
    int nearest_active_dist(int u) const;
    int tree_depth() const;
    const CentroidResult& metadata() const { return meta_; }

private:
    int n_;
    std::vector<std::vector<int>> adj_;
    CentroidResult meta_;
    std::vector<int> min_dist_;
};

void validate_tree(int n, const std::vector<std::pair<int, int>>& edges);
std::vector<int> fast_batch_nearest(const CentroidOracle& oracle, const std::vector<int>& queries);
std::vector<int> parallel_multi_query(int n, const std::vector<std::pair<int, int>>& edges,
                                      const std::vector<int>& actives, const std::vector<int>& queries);
void verify_centroid_depth(const CentroidResult& res, int n);
} // namespace codes_centroid_decomposition_tree
