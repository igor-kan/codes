#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_min_enclosing_circle_welzl;
    validate_problem_size(1);
    auto d = minimum_enclosing_disk({{0, 0}, {4, 0}, {0, 4}, {2, 1}});
    assert(std::fabs(d.cx - 2.0) < 1e-9 && std::fabs(d.cy - 2.0) < 1e-9);
    assert(std::fabs(d.r - std::sqrt(8.0)) < 1e-9);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
