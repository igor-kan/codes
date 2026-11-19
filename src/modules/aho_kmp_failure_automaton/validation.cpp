#include "interface.hpp"

namespace codes_aho_kmp_failure_automaton {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("aho_kmp_failure_automaton: problem size must be positive");
    }
}

} // namespace codes_aho_kmp_failure_automaton
