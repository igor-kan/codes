#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_suffix_automaton_lcs {
class SuffixAutomatonLcs {
public:
    explicit SuffixAutomatonLcs(const std::string& s);
    std::int64_t count_distinct_substrings() const;
    int longest_common_substring(const std::string& t) const;
private:
    std::vector<SamState> st_;
    int last_ = 0;
    void extend(int c);
};

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_suffix_automaton_lcs
