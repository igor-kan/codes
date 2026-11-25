#include "interface.hpp"

namespace codes_fenwick_2d_bit_d60 {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_fenwick_2d_bit_d60
