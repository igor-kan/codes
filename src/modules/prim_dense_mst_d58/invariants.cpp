#include "interface.hpp"

namespace codes_prim_dense_mst_d58 {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_prim_dense_mst_d58
