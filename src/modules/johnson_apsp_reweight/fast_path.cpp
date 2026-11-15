#include "interface.hpp"
// Non-negative transformed weights permit O((V+E) log V) binary-heap Dijkstra sweeps.
#include <cmath>
namespace codes_johnson_apsp_reweight {
double potential_gap_norm(const std::vector<double>& h) {
    double s = 0.0;
    for (double v : h) s += std::abs(v);
    return s;
}
} // namespace codes_johnson_apsp_reweight
