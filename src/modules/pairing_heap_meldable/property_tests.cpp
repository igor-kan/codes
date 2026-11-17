#include "interface.hpp"
#include <algorithm>
#include <cassert>

int main() {
    using namespace codes_pairing_heap_meldable;
    std::vector<std::int64_t> xs;
    for (int i = 0; i < 60; ++i) xs.push_back((i * 37 + 19) % 100);
    auto sorted_heap = fast_heapsort_pairing(xs);
    auto sorted_ref = xs;
    std::sort(sorted_ref.begin(), sorted_ref.end());
    assert(sorted_heap == sorted_ref);
    auto par = parallel_sort_chunks({{9, 1, 5, 2}, {8, 7, 3, 4}});
    assert((par[0] == std::vector<std::int64_t>{1, 2, 5, 9}));
    assert((par[1] == std::vector<std::int64_t>{3, 4, 7, 8}));
    return 0;
}
