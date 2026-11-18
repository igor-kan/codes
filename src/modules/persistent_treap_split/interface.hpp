#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_persistent_treap_split {
class PersistentTreap {
public:
    PersistentTreap() = default;
    int new_node(std::int64_t val, std::uint32_t prio);
    int clone_node(int u);
    void pull(int u);
    std::pair<int, int> split(int root, int k);
    int merge(int a, int b);
    std::int64_t range_sum(int root, int l, int r);
    int size_of(int u) const { return u < 0 ? 0 : pool_[u].sz; }
private:
    std::vector<PTreapNode> pool_;
};

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_persistent_treap_split
