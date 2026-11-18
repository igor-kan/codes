#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_polygonal_ear_clipping {
double polygon_signed_area2(const std::vector<Vec2>& poly);
std::vector<TriIdx> ear_clip_triangulate(const std::vector<Vec2>& poly);

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_polygonal_ear_clipping
