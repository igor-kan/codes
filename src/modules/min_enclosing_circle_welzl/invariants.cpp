#include "interface.hpp"

namespace codes_min_enclosing_circle_welzl {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_min_enclosing_circle_welzl
