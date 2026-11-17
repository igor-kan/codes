#include "interface.hpp"
#include <algorithm>
#include <cassert>
#include <numeric>

int main() {
    using namespace codes_hungarian_assignment_dense;
    std::vector<std::vector<std::int64_t>> c = {{4, 1, 3}, {2, 0, 5}, {3, 2, 2}};
    auto sols = parallel_solve_assignments({c, {{10, 20}, {30, 15}}});
    verify_assignment_valid(c, sols[0]);
    std::vector<int> perm = {0, 1, 2};
    std::int64_t brute = 1'000'000'000LL;
    do {
        brute = std::min(brute, c[0][perm[0]] + c[1][perm[1]] + c[2][perm[2]]);
    } while (std::next_permutation(perm.begin(), perm.end()));
    assert(sols[0].total_cost == brute);
    assert(sols[1].total_cost == 25);
    return 0;
}
