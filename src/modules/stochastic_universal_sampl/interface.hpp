#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_stochastic_universal_sampl {
class VoseAliasSampler {
public:
    explicit VoseAliasSampler(const std::vector<double>& weights);
    int sample_one(int bucket, double u01) const;
    std::vector<int> stochastic_universal(const std::vector<double>& weights, int m, double u0) const;
private:
    std::vector<AliasBucket> table_;
};

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_stochastic_universal_sampl
