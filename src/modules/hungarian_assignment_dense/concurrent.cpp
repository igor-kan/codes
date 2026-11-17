#include "interface.hpp"
#include <thread>

namespace codes_hungarian_assignment_dense {
std::vector<AssignmentSolution> parallel_solve_assignments(
    const std::vector<std::vector<std::vector<std::int64_t>>>& matrices
) {
    std::vector<AssignmentSolution> out(matrices.size());
    std::size_t mid = matrices.size() / 2;
    auto worker = [&](std::size_t lo, std::size_t hi) {
        for (std::size_t i = lo; i < hi; ++i) out[i] = solve_min_assignment(matrices[i]);
    };
    std::thread t1(worker, 0, mid);
    std::thread t2(worker, mid, matrices.size());
    t1.join();
    t2.join();
    return out;
}
} // namespace codes_hungarian_assignment_dense
