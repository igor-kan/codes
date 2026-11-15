#include "interface.hpp"
#include <cmath>

namespace codes_johnson_apsp_reweight {
Status verify_matrix_invariants(const JohnsonOutput& out) {
    if (out.has_negative_cycle) return Status::Ok;
    for (std::size_t i = 0; i < out.dist.size(); ++i) {
        if (std::abs(out.dist[i][i]) > 1e-9) return Status::InvariantViolation;
    }
    return Status::Ok;
}
} // namespace codes_johnson_apsp_reweight
