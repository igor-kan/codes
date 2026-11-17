#include "interface.hpp"

namespace codes_centroid_decomposition_tree {
std::vector<int> fast_batch_nearest(const CentroidOracle& oracle, const std::vector<int>& queries) {
    std::vector<int> ans;
    ans.reserve(queries.size());
    for (int q : queries) ans.push_back(oracle.nearest_active_dist(q));
    return ans;
}
} // namespace codes_centroid_decomposition_tree
