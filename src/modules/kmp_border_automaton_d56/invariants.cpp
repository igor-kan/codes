#include "interface.hpp"

namespace codes_kmp_border_automaton_d56 {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_kmp_border_automaton_d56
