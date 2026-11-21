#include "interface.hpp"

namespace codes_dijkstra_minheap_sp {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("dijkstra_minheap_sp: problem size must be positive");
    }
}

} // namespace codes_dijkstra_minheap_sp
