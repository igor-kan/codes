#include "interface.hpp"

namespace codes_centroid_tree_dist_d57 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("centroid_tree_dist_d57: problem size must be positive");
    }
}

} // namespace codes_centroid_tree_dist_d57
