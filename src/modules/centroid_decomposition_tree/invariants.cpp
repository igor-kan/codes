#include "interface.hpp"

namespace codes_centroid_decomposition_tree {
void verify_centroid_depth(const CentroidResult& res, int n) {
    int limit = 1;
    int p = n;
    while (p > 1) { p >>= 1; ++limit; }
    for (int d : res.depth) {
        if (d < 0 || d > limit) throw std::logic_error("centroid depth violated O(log N) bound");
    }
}
} // namespace codes_centroid_decomposition_tree
