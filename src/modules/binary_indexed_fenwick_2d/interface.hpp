#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_binary_indexed_fenwick_2d {
class Fenwick2D {
public:
    Fenwick2D(int rows, int cols);
    void add(int r, int c, long long delta);
    long long prefix_sum(int r, int c) const;
    long long rect_sum(int r1, int c1, int r2, int c2) const;
private:
    int rows_;
    int cols_;
    std::vector<long long> bit_;
};

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_binary_indexed_fenwick_2d
