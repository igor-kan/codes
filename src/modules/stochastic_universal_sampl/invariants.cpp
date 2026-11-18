#include "interface.hpp"

namespace codes_stochastic_universal_sampl {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_stochastic_universal_sampl
