#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_matrix_path_count_d59;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<std::vector<long long>> k3 = {{0,1,1},{1,0,1},{1,1,0}};
    auto r = count_k_walks(k3, 3);
    long long sum = r[0][0] + r[0][1] + r[0][2];
    assert(sum == 8);
    return 0;
}
