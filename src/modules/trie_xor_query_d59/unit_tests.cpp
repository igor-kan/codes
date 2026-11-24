#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_trie_xor_query_d59;
    validate_problem_size(1);
    XorTrie tr;
    for (unsigned v : {3u, 10u, 5u, 25u, 2u, 8u}) tr.insert(v);
    assert(tr.max_xor(5u) == 28u && tr.max_xor(25u) == 28u);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
