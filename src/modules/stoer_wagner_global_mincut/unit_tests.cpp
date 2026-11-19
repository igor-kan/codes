#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_stoer_wagner_global_mincut;
    validate_problem_size(1);
    std::vector<std::vector<std::int64_t>> g = {
        {0, 2, 0, 0, 3}, {2, 0, 3, 0, 2}, {0, 3, 0, 4, 0}, {0, 0, 4, 0, 1}, {3, 2, 0, 1, 0}
    };
    auto res = stoer_wagner_mincut(5, g);
    assert(res.weight == 4 && res.phases == 4);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
