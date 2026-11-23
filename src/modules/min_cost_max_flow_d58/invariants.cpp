#include "interface.hpp"

namespace codes_min_cost_max_flow_d58 {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_min_cost_max_flow_d58
