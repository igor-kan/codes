#include "interface.hpp"
#include <cmath>

namespace codes_floyd_warshall_apsp {
Status validate_matrix(std::size_t n, const std::vector<double>& adj) {
    if (adj.size() != n * n) return Status::OutOfBounds;
    for (double w : adj) {
        if (std::isnan(w)) return Status::InvalidInput;
    }
    return Status::Ok;
}
} // namespace codes_floyd_warshall_apsp
