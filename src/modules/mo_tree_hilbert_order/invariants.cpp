#include "interface.hpp"

namespace codes_mo_tree_hilbert_order {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_mo_tree_hilbert_order
