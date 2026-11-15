#include "interface.hpp"
#include <limits>

namespace codes_floyd_warshall_apsp {
ApspResult solve_apsp_blocked(std::size_t n, const std::vector<double>& adj_weights) {
    // Pointer-cached inner j-loop minimizes index arithmetic on contiguous row slices
    const double INF = std::numeric_limits<double>::infinity();
    ApspResult res;
    res.n = n;
    res.dist = adj_weights;
    res.next_hop.assign(n * n, -1);
    for (std::size_t k = 0; k < n; ++k) {
        const double* row_k = res.dist.data() + k * n;
        for (std::size_t i = 0; i < n; ++i) {
            double* row_i = res.dist.data() + i * n;
            const double dik = row_i[k];
            if (dik == INF) continue;
            for (std::size_t j = 0; j < n; ++j) {
                double cand = dik + row_k[j];
                if (cand < row_i[j]) row_i[j] = cand;
            }
        }
    }
    for (std::size_t i = 0; i < n; ++i) {
        if (res.dist[i * n + i] < -1e-12) { res.has_negative_cycle = true; break; }
    }
    return res;
}
} // namespace codes_floyd_warshall_apsp
