#include "interface.hpp"

namespace codes_two_sat_implication {
bool fast_verify_assignment(const std::vector<Clause2>& clauses, const std::vector<bool>& assign) {
    for (const auto& c : clauses) {
        bool va = assign[static_cast<std::size_t>(c.var_a)] ^ c.neg_a;
        bool vb = assign[static_cast<std::size_t>(c.var_b)] ^ c.neg_b;
        if (!va && !vb) return false;
    }
    return true;
}
} // namespace codes_two_sat_implication
