#include "interface.hpp"

namespace codes_persistent_treap_split {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_persistent_treap_split
