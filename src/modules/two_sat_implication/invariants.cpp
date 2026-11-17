#include "interface.hpp"

namespace codes_two_sat_implication {
void verify_sat_witness(int n, const std::vector<Clause2>& clauses, const SatResult& res) {
    if (res.satisfiable) {
        if (static_cast<int>(res.assignment.size()) != n || !fast_verify_assignment(clauses, res.assignment)) {
            throw std::logic_error("2-SAT returned invalid satisfying assignment");
        }
    }
}
} // namespace codes_two_sat_implication
