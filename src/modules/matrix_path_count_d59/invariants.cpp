#include "interface.hpp"

namespace codes_matrix_path_count_d59 {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_matrix_path_count_d59
