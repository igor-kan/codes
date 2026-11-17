#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_two_sat_implication {
class TwoSatSolver {
public:
    explicit TwoSatSolver(int num_vars);
    void add_or(int va, bool na, int vb, bool nb);
    void add_xor(int va, int vb);
    void force_true(int v, bool neg = false);
    SatResult solve() const;
    int num_vars() const { return n_; }

private:
    int n_;
    std::vector<Clause2> clauses_;
};

void validate_clause_vars(int n, const Clause2& c);
bool fast_verify_assignment(const std::vector<Clause2>& clauses, const std::vector<bool>& assign);
std::vector<SatResult> parallel_solve_instances(const std::vector<std::pair<int, std::vector<Clause2>>>& batch);
void verify_sat_witness(int n, const std::vector<Clause2>& clauses, const SatResult& res);
} // namespace codes_two_sat_implication
