#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_mo_offline_queries;
    std::vector<int> arr = {1, 2, 1, 3, 2, 4, 1, 5};
    std::vector<RangeQuery> q = {{0, 2, 0}, {1, 5, 1}, {0, 7, 2}, {3, 3, 3}};
    auto r = answer_distinct_queries(arr, q);
    assert((r == std::vector<std::size_t>{2, 4, 5, 1}));
    assert(verify_agreement(arr, q) == Status::Ok);
    return 0;
}
