#include "interface.hpp"

namespace codes_binary_indexed_fenwick_2d {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_binary_indexed_fenwick_2d
