#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_dsu_bipartite_parity_d59 {
class BipartiteDsu {
public:
    explicit BipartiteDsu(int n);
    bool add_edge(int u, int v);
    bool is_bipartite() const { return ok_; }
private:
    std::vector<int> p_;
    std::vector<int> col_;
    bool ok_ = true;
    std::pair<int, int> find(int x);
};

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_dsu_bipartite_parity_d59
