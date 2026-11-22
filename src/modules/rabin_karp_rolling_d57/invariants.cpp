#include "interface.hpp"

namespace codes_rabin_karp_rolling_d57 {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_rabin_karp_rolling_d57
