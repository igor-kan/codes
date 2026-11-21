#include "interface.hpp"

namespace codes_kmp_border_automaton_d56 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("kmp_border_automaton_d56: problem size must be positive");
    }
}

} // namespace codes_kmp_border_automaton_d56
