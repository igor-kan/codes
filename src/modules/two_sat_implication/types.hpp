#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_two_sat_implication {
struct Clause2 {
    int var_a;
    bool neg_a;
    int var_b;
    bool neg_b;
};

struct SatResult {
    bool satisfiable;
    std::vector<bool> assignment;
};
} // namespace codes_two_sat_implication
