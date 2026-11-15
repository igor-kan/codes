#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_bellman_ford_spfa {
struct Edge { std::size_t to; double w; };
struct SsspResult {
    std::vector<double> dist;
    std::vector<int> parent;
    bool negative_cycle = false;
};
} // namespace codes_bellman_ford_spfa
