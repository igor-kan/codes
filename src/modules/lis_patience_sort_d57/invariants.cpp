#include "interface.hpp"

namespace codes_lis_patience_sort_d57 {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_lis_patience_sort_d57
