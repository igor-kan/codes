#include "interface.hpp"

namespace codes_manacher_palindrome_radii {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("manacher_palindrome_radii: problem size must be positive");
    }
}

} // namespace codes_manacher_palindrome_radii
