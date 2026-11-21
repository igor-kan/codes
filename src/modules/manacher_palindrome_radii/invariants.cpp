#include "interface.hpp"

namespace codes_manacher_palindrome_radii {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_manacher_palindrome_radii
