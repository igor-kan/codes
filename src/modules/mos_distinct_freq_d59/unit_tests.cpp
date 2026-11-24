#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_mos_distinct_freq_d59;
    validate_problem_size(1);
    auto res = count_equal_pairs_queries({1, 2, 1, 1, 2}, {{0, 3}, {1, 4}, {0, 4}});
    assert((res == std::vector<long long>{3, 2, 4}));
    verify_module_postcondition(true, "unit ok");
    return 0;
}
