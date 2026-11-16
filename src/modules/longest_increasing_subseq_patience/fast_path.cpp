#include "interface.hpp"
#include <algorithm>

namespace codes_longest_increasing_subseq_patience {
std::size_t compute_lis_length_fast(const std::vector<int64_t>& seq) {
    std::vector<int64_t> tails;
    tails.reserve(seq.size());
    for (int64_t x : seq) {
        auto it = std::lower_bound(tails.begin(), tails.end(), x);
        if (it == tails.end()) tails.push_back(x);
        else *it = x;
    }
    return tails.size();
}
} // namespace codes_longest_increasing_subseq_patience
