#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_lis_patience_sort_d57;
    validate_problem_size(1);
    assert(patience_lis_length({10, 9, 2, 5, 3, 7, 101, 18}) == 4);
    assert(patience_lis_length({7, 7, 7, 7}) == 1);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
