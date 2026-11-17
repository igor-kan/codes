#include "interface.hpp"
#include <algorithm>

namespace codes_two_sat_implication {

TwoSatSolver::TwoSatSolver(int num_vars) : n_(num_vars) {
    if (num_vars <= 0) throw std::invalid_argument("variable count must be positive");
}

void TwoSatSolver::add_or(int va, bool na, int vb, bool nb) {
    Clause2 c{va, na, vb, nb};
    validate_clause_vars(n_, c);
    clauses_.push_back(c);
}

void TwoSatSolver::add_xor(int va, int vb) {
    add_or(va, false, vb, false);
    add_or(va, true, vb, true);
}

void TwoSatSolver::force_true(int v, bool neg) {
    add_or(v, neg, v, neg);
}

SatResult TwoSatSolver::solve() const {
    int nodes = 2 * n_;
    std::vector<std::vector<int>> adj(static_cast<std::size_t>(nodes));
    auto lit = [](int v, bool neg) -> int { return 2 * v + (neg ? 1 : 0); };
    for (const auto& c : clauses_) {
        int a = lit(c.var_a, c.neg_a);
        int b = lit(c.var_b, c.neg_b);
        adj[static_cast<std::size_t>(a ^ 1)].push_back(b);
        adj[static_cast<std::size_t>(b ^ 1)].push_back(a);
    }

    std::vector<int> dfn(static_cast<std::size_t>(nodes), -1);
    std::vector<int> low(static_cast<std::size_t>(nodes), 0);
    std::vector<int> comp(static_cast<std::size_t>(nodes), -1);
    std::vector<bool> on_st(static_cast<std::size_t>(nodes), false);
    std::vector<int> st;
    int timer = 0;
    int scc_cnt = 0;

    auto dfs = [&](auto& self, int u) -> void {
        dfn[static_cast<std::size_t>(u)] = low[static_cast<std::size_t>(u)] = timer++;
        st.push_back(u);
        on_st[static_cast<std::size_t>(u)] = true;
        for (int w : adj[static_cast<std::size_t>(u)]) {
            if (dfn[static_cast<std::size_t>(w)] == -1) {
                self(self, w);
                low[static_cast<std::size_t>(u)] = std::min(low[static_cast<std::size_t>(u)], low[static_cast<std::size_t>(w)]);
            } else if (on_st[static_cast<std::size_t>(w)]) {
                low[static_cast<std::size_t>(u)] = std::min(low[static_cast<std::size_t>(u)], dfn[static_cast<std::size_t>(w)]);
            }
        }
        if (low[static_cast<std::size_t>(u)] == dfn[static_cast<std::size_t>(u)]) {
            while (true) {
                int v = st.back();
                st.pop_back();
                on_st[static_cast<std::size_t>(v)] = false;
                comp[static_cast<std::size_t>(v)] = scc_cnt;
                if (v == u) break;
            }
            ++scc_cnt;
        }
    };

    for (int i = 0; i < nodes; ++i) {
        if (dfn[static_cast<std::size_t>(i)] == -1) dfs(dfs, i);
    }
    SatResult res;
    res.assignment.assign(static_cast<std::size_t>(n_), false);
    for (int i = 0; i < n_; ++i) {
        int ct = comp[static_cast<std::size_t>(2 * i)];
        int cf = comp[static_cast<std::size_t>(2 * i + 1)];
        if (ct == cf) {
            res.satisfiable = false;
            res.assignment.clear();
            return res;
        }
        res.assignment[static_cast<std::size_t>(i)] = (ct < cf);
    }
    res.satisfiable = true;
    return res;
}

} // namespace codes_two_sat_implication
