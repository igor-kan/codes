#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_kmp_border_automaton_d56;
    validate_problem_size(1);
    auto pi = kmp_prefix_function("ababa");
    assert((pi == std::vector<int>{0, 0, 1, 2, 3}));
    auto hits = kmp_find_all("abababa", "aba");
    assert((hits == std::vector<int>{0, 2, 4}));
    verify_module_postcondition(true, "unit ok");
    return 0;
}
