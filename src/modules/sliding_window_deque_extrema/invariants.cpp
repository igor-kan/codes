#include "interface.hpp"

namespace codes_sliding_window_deque_extrema {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_sliding_window_deque_extrema
