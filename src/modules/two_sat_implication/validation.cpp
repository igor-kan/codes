#include "interface.hpp"

namespace codes_two_sat_implication {
void validate_clause_vars(int n, const Clause2& c) {
    if (c.var_a < 0 || c.var_a >= n || c.var_b < 0 || c.var_b >= n) {
        throw std::out_of_range("2-SAT variable index out of bounds");
    }
}
} // namespace codes_two_sat_implication
