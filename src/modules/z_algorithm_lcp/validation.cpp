#include "interface.hpp"

namespace codes_z_algorithm_lcp {
Status validate_inputs(const std::string& text, const std::string& pattern) {
    if (pattern.empty()) return Status::NullOrEmpty;
    if (pattern.size() > (1U << 20)) return Status::OutOfBounds;
    if (text.empty() && !pattern.empty()) return Status::Ok;
    return Status::Ok;
}
} // namespace codes_z_algorithm_lcp
