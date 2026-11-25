#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_aho_corasick_dfa_d60;
    validate_problem_size(1);
    AhoCorasick ac;
    ac.add_pattern("he");
    ac.add_pattern("she");
    ac.add_pattern("hers");
    ac.add_pattern("his");
    ac.build();
    assert(ac.count_matches("ahishers") == 4);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
