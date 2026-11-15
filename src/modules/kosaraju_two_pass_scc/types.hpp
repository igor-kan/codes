#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_kosaraju_two_pass_scc {
struct SccResult {
    std::size_t num_components = 0;
    std::vector<std::size_t> comp_id;
};
} // namespace codes_kosaraju_two_pass_scc
