#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_sliding_window_deque_extrema;
    validate_problem_size(1);
    std::vector<long long> xs = {1, 3, -1, -3, 5, 3, 6, 7};
    assert((sliding_window_max(xs, 3) == std::vector<long long>{3, 3, 5, 5, 6, 7}));
    assert((sliding_window_min(xs, 3) == std::vector<long long>{-1, -3, -3, -3, 3, 3}));
    verify_module_postcondition(true, "unit ok");
    return 0;
}
