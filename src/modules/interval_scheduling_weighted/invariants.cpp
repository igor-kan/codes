#include "interface.hpp"

namespace codes_interval_scheduling_weighted {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_interval_scheduling_weighted
