#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_knapsack_bounded_dp_d57;
    validate_problem_size(1);
    std::vector<BoundedBundle> its = {{3, 40, 2}, {4, 50, 1}, {2, 25, 3}};
    assert(bounded_knapsack_max(8, its) == 105);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
