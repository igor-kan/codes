#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_rabin_karp_rolling_d57;
    validate_problem_size(1);
    auto h = rabin_karp_search("abracadabra", "abra");
    assert((h == std::vector<int>{0, 7}));
    verify_module_postcondition(true, "unit ok");
    return 0;
}
