#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_prim_dense_mst_d58 {

long long prim_dense_mst(const std::vector<std::vector<long long>>& mat) {
    int n = static_cast<int>(mat.size());
    if (n <= 0) throw std::invalid_argument("empty matrix");
    const long long INF = 1000000000000000LL;
    std::vector<long long> min_e(n, INF);
    std::vector<bool> used(n, false);
    min_e[0] = 0;
    long long total = 0;
    for (int it = 0; it < n; ++it) {
        int v = -1;
        for (int j = 0; j < n; ++j) {
            if (!used[j] && (v == -1 || min_e[j] < min_e[v])) v = j;
        }
        if (min_e[v] >= INF) throw std::invalid_argument("disconnected graph");
        used[v] = true;
        total += min_e[v];
        for (int to = 0; to < n; ++to) {
            if (!used[to] && mat[v][to] < min_e[to]) min_e[to] = mat[v][to];
        }
    }
    return total;
}

} // namespace codes_prim_dense_mst_d58
