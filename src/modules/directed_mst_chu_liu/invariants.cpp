#include "interface.hpp"

namespace codes_directed_mst_chu_liu {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_directed_mst_chu_liu
