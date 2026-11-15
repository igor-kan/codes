#include "interface.hpp"
#include <limits>
#include <queue>
#include <thread>

namespace codes_johnson_apsp_reweight {
JohnsonOutput solve_johnson_mt(std::size_t n, const std::vector<std::vector<WEdge>>& adj) {
    return solve_johnson(n, adj);
}
} // namespace codes_johnson_apsp_reweight
