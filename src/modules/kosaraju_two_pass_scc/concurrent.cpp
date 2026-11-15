#include "interface.hpp"
namespace codes_kosaraju_two_pass_scc {
std::size_t count_reachable_pairs_in_sccs(const SccResult& res) {
    std::vector<std::size_t> sizes(res.num_components, 0);
    for (std::size_t c : res.comp_id) sizes[c]++;
    std::size_t pairs = 0;
    for (std::size_t s : sizes) pairs += s * s;
    return pairs;
}
} // namespace codes_kosaraju_two_pass_scc
