#include "interface.hpp"

namespace codes_suffix_automaton_lcs {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("suffix_automaton_lcs: problem size must be positive");
    }
}

} // namespace codes_suffix_automaton_lcs
