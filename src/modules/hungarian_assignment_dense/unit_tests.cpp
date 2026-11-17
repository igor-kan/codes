#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_hungarian_assignment_dense;
    std::vector<std::vector<std::int64_t>> c = {
        {9, 2, 7, 8},
        {6, 4, 3, 7},
        {5, 8, 1, 8},
        {7, 6, 9, 4}
    };
    auto sol = solve_min_assignment(c);
    verify_assignment_valid(c, sol);
    assert(sol.total_cost == 13);
    return 0;
}
