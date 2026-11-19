#include "interface.hpp"

namespace codes_zkw_segment_iter_cpp {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_zkw_segment_iter_cpp
