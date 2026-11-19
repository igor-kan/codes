#include "interface.hpp"

namespace codes_pollard_rho_brent_u128 {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_pollard_rho_brent_u128
