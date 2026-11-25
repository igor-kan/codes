#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_aho_corasick_dfa_d60 {
class AhoCorasick {
    std::vector<AcNode> nodes_;
    bool built_;
public:
    AhoCorasick();
    void add_pattern(const std::string& pat);
    void build();
    int count_matches(const std::string& text) const;
};

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_aho_corasick_dfa_d60
