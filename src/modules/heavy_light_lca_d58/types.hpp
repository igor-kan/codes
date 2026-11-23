#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_heavy_light_lca_d58 {
struct LcaJumpSpec {
    int nodes = 0;
    int log_max = 16;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "heavy_light_lca_d58";
    int version = 1;
};
} // namespace codes_heavy_light_lca_d58
