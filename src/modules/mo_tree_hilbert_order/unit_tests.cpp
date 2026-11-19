#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_mo_tree_hilbert_order;
    validate_problem_size(1);
    auto res = mo_distinct_queries({1, 2, 1, 3, 2, 4, 4}, {{0, 2}, {1, 5}, {4, 6}});
    assert((res == std::vector<int>{2, 4, 2}));
    verify_module_postcondition(true, "unit ok");
    return 0;
}
