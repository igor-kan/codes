#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_hungarian_assignment_dense {
AssignmentSolution solve_min_assignment(const std::vector<std::vector<std::int64_t>>& cost);
void validate_cost_matrix(const std::vector<std::vector<std::int64_t>>& cost);
std::int64_t fast_eval_assignment(const std::vector<std::vector<std::int64_t>>& cost, const std::vector<int>& assign);
std::vector<AssignmentSolution> parallel_solve_assignments(
    const std::vector<std::vector<std::vector<std::int64_t>>>& matrices);
void verify_assignment_valid(const std::vector<std::vector<std::int64_t>>& cost, const AssignmentSolution& sol);
} // namespace codes_hungarian_assignment_dense
