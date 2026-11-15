#include "interface.hpp"
namespace codes_kosaraju_two_pass_scc {
SccResult find_scc_iterative(std::size_t n, const std::vector<std::vector<std::size_t>>& adj) {
    return find_scc(n, adj);
}
} // namespace codes_kosaraju_two_pass_scc
