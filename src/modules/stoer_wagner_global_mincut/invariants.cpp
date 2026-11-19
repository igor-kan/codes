#include "interface.hpp"

namespace codes_stoer_wagner_global_mincut {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_stoer_wagner_global_mincut
