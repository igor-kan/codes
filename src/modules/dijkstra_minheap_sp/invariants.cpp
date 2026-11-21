#include "interface.hpp"

namespace codes_dijkstra_minheap_sp {

void verify_module_postcondition(bool ok, const char* msg) {
    if (!ok) {
        throw std::logic_error(msg);
    }
}

} // namespace codes_dijkstra_minheap_sp
