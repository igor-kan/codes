#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_rolling_median_multiset_d58;
    validate_problem_size(1);
    std::vector<long long> xs = {1, 3, -1, -3, 5, 3, 6, 7};
    assert((sliding_window_medians(xs, 3) == std::vector<long long>{1, -1, -1, 3, 5, 6}));
    verify_module_postcondition(true, "unit ok");
    return 0;
}
