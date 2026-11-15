#include "interface.hpp"
namespace codes_bellman_ford_spfa {
Status validate_graph(std::size_t n, std::size_t src) {
    return (n > 0 && src < n) ? Status::Ok : Status::OutOfBounds;
}
} // namespace codes_bellman_ford_spfa
