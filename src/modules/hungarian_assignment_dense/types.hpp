#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_hungarian_assignment_dense {
struct AssignmentSolution {
    std::int64_t total_cost;
    std::vector<int> row_to_col;
};
} // namespace codes_hungarian_assignment_dense
