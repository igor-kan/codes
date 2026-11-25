#include "interface.hpp"

namespace codes_tarjan_bridge_cut_d60 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("tarjan_bridge_cut_d60: problem size must be positive");
    }
}

} // namespace codes_tarjan_bridge_cut_d60
