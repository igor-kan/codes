#include "interface.hpp"

namespace codes_cartesian_tree_rmq_lca {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_cartesian_tree_rmq_lca
