#include "interface.hpp"

namespace codes_trie_xor_query_d59 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("trie_xor_query_d59: problem size must be positive");
    }
}

} // namespace codes_trie_xor_query_d59
