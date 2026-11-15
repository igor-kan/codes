#include "interface.hpp"

namespace codes_z_algorithm_lcp {
Status verify_z_invariants(const std::string& s, const std::vector<std::size_t>& z) {
    if (z.size() != s.size()) return Status::InvariantViolation;
    if (s.empty()) return Status::Ok;
    if (z[0] != s.size()) return Status::InvariantViolation;
    for (std::size_t i = 1; i < s.size(); ++i) {
        if (i + z[i] > s.size()) return Status::InvariantViolation;
        for (std::size_t k = 0; k < z[i]; ++k) {
            if (s[k] != s[i + k]) return Status::InvariantViolation;
        }
        if (i + z[i] < s.size() && s[z[i]] == s[i + z[i]]) return Status::InvariantViolation;
    }
    return Status::Ok;
}
} // namespace codes_z_algorithm_lcp
