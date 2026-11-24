#include "interface.hpp"

namespace codes_mos_distinct_freq_d59 {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_mos_distinct_freq_d59
