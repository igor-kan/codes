#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_johnson_apsp_reweight {
struct WEdge { std::size_t to; double w; };
struct JohnsonOutput {
    std::vector<double> potentials;
    std::vector<std::vector<double>> dist;
    bool has_negative_cycle = false;
};
} // namespace codes_johnson_apsp_reweight
