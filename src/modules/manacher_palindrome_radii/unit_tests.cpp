#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_manacher_palindrome_radii;
    validate_problem_size(1);
    assert(manacher_longest_palindrome("babad").size() == 3);
    assert(manacher_longest_palindrome("cbbd") == "bb");
    assert(manacher_longest_palindrome("racecar") == "racecar");
    verify_module_postcondition(true, "unit ok");
    return 0;
}
