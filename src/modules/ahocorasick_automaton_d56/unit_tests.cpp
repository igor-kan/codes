#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_ahocorasick_automaton_d56;
    validate_problem_size(1);
    std::vector<std::string> pats = {"he", "she", "hers", "his"};
    assert(ac_count_matches(pats, "ahishers") == 4);
    auto per = ac_per_pattern_hits(pats, "ahishers");
    assert(per[0] == 1 && per[1] == 1 && per[2] == 1 && per[3] == 1);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
