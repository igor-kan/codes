#include "interface.hpp"

namespace codes_aho_corasick_dfa_d60 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("aho_corasick_dfa_d60: problem size must be positive");
    }
}

} // namespace codes_aho_corasick_dfa_d60
