#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_min_enclosing_circle_welzl {
Disk2D disk_from_two(Point2D a, Point2D b);
Disk2D disk_from_three(Point2D a, Point2D b, Point2D c);
Disk2D minimum_enclosing_disk(const std::vector<Point2D>& pts);

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_min_enclosing_circle_welzl
