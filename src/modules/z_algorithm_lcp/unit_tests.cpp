#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_z_algorithm_lcp;
    const std::string s = "aabxaabxcaabxaabxay";
    auto z = compute_z_array(s);
    assert(z[0] == s.size() && z[1] == 1 && z[4] == 4 && z[9] == 8);
    assert(verify_z_invariants(s, z) == Status::Ok);
    auto m = find_matches("abababa", "aba");
    assert((m == std::vector<std::size_t>{0, 2, 4}));
    auto batch = batch_find_matches({"abcabc", "zzzz"}, "abc");
    assert((batch[0] == std::vector<std::size_t>{0, 3}) && batch[1].empty());
    return 0;
}
