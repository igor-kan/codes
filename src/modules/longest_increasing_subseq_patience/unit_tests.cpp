#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_longest_increasing_subseq_patience;
    std::vector<int64_t> a = {10, 9, 2, 5, 3, 7, 101, 18};
    auto r = compute_lis_patience(a);
    assert(r.values.size() == 4);
    assert(compute_lis_length_fast(a) == 4);
    assert(verify_lis_invariants(a, r) == Status::Ok);

    std::vector<int64_t> eq = {5, 5, 5, 5};
    auto re = compute_lis_patience(eq);
    assert(re.values.size() == 1);
    assert(verify_lis_invariants(eq, re) == Status::Ok);
    return 0;
}
