#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_fenwick_2d_bit_d60 {
class Fenwick2D {
    int rows_, cols_;
    std::vector<std::vector<std::int64_t>> bit_;
public:
    Fenwick2D(int r, int c);
    void add(int r, int c, std::int64_t delta);
    std::int64_t prefix_sum(int r, int c) const;
    std::int64_t rect_sum(int r1, int c1, int r2, int c2) const;
};

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_fenwick_2d_bit_d60
