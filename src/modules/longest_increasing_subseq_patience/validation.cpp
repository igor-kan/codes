#include "interface.hpp"

namespace codes_longest_increasing_subseq_patience {
Status validate_sequence(const std::vector<int64_t>& seq) {
    if (seq.empty()) return Status::NullOrEmpty;
    return Status::Ok;
}
} // namespace codes_longest_increasing_subseq_patience
