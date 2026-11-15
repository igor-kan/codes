#include "interface.hpp"
#include <thread>

namespace codes_floyd_warshall_apsp {
Status batch_verify_paths(const ApspResult& res) {
    if (res.has_negative_cycle) return Status::Ok;
    for (std::size_t u = 0; u < res.n; ++u) {
        for (std::size_t v = 0; v < res.n; ++v) {
            if (res.next_hop[u * res.n + v] != -1) {
                auto p = reconstruct_path(res, u, v);
                if (p.empty() || static_cast<std::size_t>(p.back()) != v) return Status::InvariantViolation;
            }
        }
    }
    return Status::Ok;
}
} // namespace codes_floyd_warshall_apsp
