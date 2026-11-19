#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_aho_kmp_failure_automaton;
    validate_problem_size(1);
    auto s = scan_ac_dfa({"he", "she", "his", "hers"}, "ushers");
    assert(s.matches == 3);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
