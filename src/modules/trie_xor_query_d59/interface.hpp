#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_trie_xor_query_d59 {
class XorTrie {
public:
    XorTrie();
    void insert(unsigned int val);
    unsigned int max_xor(unsigned int q) const;
private:
    std::vector<XorNode> nodes_;
};

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_trie_xor_query_d59
