#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_stochastic_universal_sampl;
    validate_problem_size(1);
    std::vector<double> w = {1.0, 2.0, 5.0};
    VoseAliasSampler vs(w);
    auto sus = vs.stochastic_universal(w, 8, 0.5);
    assert(sus.size() == 8 && sus.front() == 0 && sus.back() == 2);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
