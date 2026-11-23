#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_bitmask_subset_dp_d58;
    validate_problem_size(1);
    std::vector<std::vector<long long>> m = {{9, 2, 7}, {6, 4, 3}, {5, 8, 1}};
    assert(min_bitmask_assignment(m) == 9);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
