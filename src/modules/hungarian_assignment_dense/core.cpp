#include "interface.hpp"
#include <algorithm>
#include <limits>

namespace codes_hungarian_assignment_dense {

AssignmentSolution solve_min_assignment(const std::vector<std::vector<std::int64_t>>& cost) {
    validate_cost_matrix(cost);
    int n = static_cast<int>(cost.size());
    int m = static_cast<int>(cost[0].size());
    const std::int64_t inf = std::numeric_limits<std::int64_t>::max() / 4;
    std::vector<std::int64_t> u(static_cast<std::size_t>(n + 1), 0);
    std::vector<std::int64_t> v(static_cast<std::size_t>(m + 1), 0);
    std::vector<int> p(static_cast<std::size_t>(m + 1), 0);
    std::vector<int> way(static_cast<std::size_t>(m + 1), 0);

    for (int i = 1; i <= n; ++i) {
        p[0] = i;
        int j0 = 0;
        std::vector<std::int64_t> minv(static_cast<std::size_t>(m + 1), inf);
        std::vector<bool> used(static_cast<std::size_t>(m + 1), false);
        do {
            used[static_cast<std::size_t>(j0)] = true;
            int i0 = p[static_cast<std::size_t>(j0)];
            std::int64_t delta = inf;
            int j1 = 0;
            for (int j = 1; j <= m; ++j) {
                if (!used[static_cast<std::size_t>(j)]) {
                    std::int64_t cur = cost[static_cast<std::size_t>(i0 - 1)][static_cast<std::size_t>(j - 1)]
                                       - u[static_cast<std::size_t>(i0)] - v[static_cast<std::size_t>(j)];
                    if (cur < minv[static_cast<std::size_t>(j)]) {
                        minv[static_cast<std::size_t>(j)] = cur;
                        way[static_cast<std::size_t>(j)] = j0;
                    }
                    if (minv[static_cast<std::size_t>(j)] < delta) {
                        delta = minv[static_cast<std::size_t>(j)];
                        j1 = j;
                    }
                }
            }
            for (int j = 0; j <= m; ++j) {
                if (used[static_cast<std::size_t>(j)]) {
                    u[static_cast<std::size_t>(p[static_cast<std::size_t>(j)])] += delta;
                    v[static_cast<std::size_t>(j)] -= delta;
                } else {
                    minv[static_cast<std::size_t>(j)] -= delta;
                }
            }
            j0 = j1;
        } while (p[static_cast<std::size_t>(j0)] != 0);
        do {
            int j1 = way[static_cast<std::size_t>(j0)];
            p[static_cast<std::size_t>(j0)] = p[static_cast<std::size_t>(j1)];
            j0 = j1;
        } while (j0 != 0);
    }

    std::vector<int> ans(static_cast<std::size_t>(n), -1);
    for (int j = 1; j <= m; ++j) {
        if (p[static_cast<std::size_t>(j)] != 0) {
            ans[static_cast<std::size_t>(p[static_cast<std::size_t>(j)] - 1)] = j - 1;
        }
    }
    return {fast_eval_assignment(cost, ans), ans};
}

} // namespace codes_hungarian_assignment_dense
