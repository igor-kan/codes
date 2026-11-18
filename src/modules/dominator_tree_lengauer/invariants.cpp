#include "interface.hpp"

namespace codes_dominator_tree_lengauer {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_dominator_tree_lengauer
