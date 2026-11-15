#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_floyd_warshall_apsp {
struct ApspResult {
    std::size_t n = 0;
    std::vector<double> dist;
    std::vector<int> next_hop;
    bool has_negative_cycle = false;
};
} // namespace codes_floyd_warshall_apsp
