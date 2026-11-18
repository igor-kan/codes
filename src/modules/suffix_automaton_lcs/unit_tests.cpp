#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_suffix_automaton_lcs;
    validate_problem_size(1);
    SuffixAutomatonLcs sam("ababa");
    assert(sam.count_distinct_substrings() == 9);
    assert(sam.longest_common_substring("babab") == 4);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
