#include "interface.hpp"
#include <limits>

namespace codes_floyd_warshall_apsp {
Status verify_triangle_inequality(const ApspResult& res) {
    if (res.has_negative_cycle) return Status::Ok;
    const std::size_t n = res.n;
    const double INF = std::numeric_limits<double>::infinity();
    for (std::size_t i = 0; i < n; ++i) {
        for (std::size_t j = 0; j < n; ++j) {
            for (std::size_t k = 0; k < n; ++k) {
                double dik = res.dist[i*n+k], dkj = res.dist[k*n+j], dij = res.dist[i*n+j];
                if (dik < INF && dkj < INF && dik + dkj + 1e-9 < dij) return Status::InvariantViolation;
            }
        }
    }
    return Status::Ok;
}
} // namespace codes_floyd_warshall_apsp
