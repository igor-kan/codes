#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_stoer_wagner_global_mincut {

CutResult stoer_wagner_mincut(int n, const std::vector<std::vector<std::int64_t>>& adj) {
    std::vector<std::vector<std::int64_t>> w = adj;
    std::vector<int> vtx(n);
    for (int i = 0; i < n; ++i) vtx[i] = i;
    std::int64_t best = std::numeric_limits<std::int64_t>::max();
    int phases = 0;
    for (int m = n; m > 1; --m) {
        std::vector<std::int64_t> weight(m, 0);
        std::vector<bool> used(m, false);
        int prev = -1, last = -1;
        for (int it = 0; it < m; ++it) {
            int sel = -1;
            for (int i = 0; i < m; ++i) {
                if (!used[i] && (sel == -1 || weight[i] > weight[sel])) sel = i;
            }
            used[sel] = true;
            prev = last;
            last = sel;
            for (int i = 0; i < m; ++i) {
                if (!used[i]) weight[i] += w[vtx[sel]][vtx[i]];
            }
        }
        best = std::min(best, weight[last]);
        ++phases;
        int u = vtx[prev], v = vtx[last];
        for (int i = 0; i < m; ++i) {
            int k = vtx[i];
            if (k != u && k != v) {
                w[u][k] += w[v][k];
                w[k][u] += w[k][v];
            }
        }
        vtx[last] = vtx[m - 1];
    }
    return {best, phases};
}

} // namespace codes_stoer_wagner_global_mincut
