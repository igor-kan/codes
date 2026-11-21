#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_interval_scheduling_weighted;
    validate_problem_size(1);
    std::vector<WeightedJob> jobs = {{1, 3, 20}, {2, 5, 20}, {3, 10, 100}, {6, 9, 50}};
    assert(max_non_overlapping_weight(jobs) == 120);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
