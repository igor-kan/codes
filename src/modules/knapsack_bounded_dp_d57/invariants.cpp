#include "interface.hpp"

namespace codes_knapsack_bounded_dp_d57 {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_knapsack_bounded_dp_d57
