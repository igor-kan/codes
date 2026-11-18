#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_directed_mst_chu_liu {
struct DirEdge {
    int u;
    int v;
    std::int64_t w;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "directed_mst_chu_liu";
    int version = 1;
};
} // namespace codes_directed_mst_chu_liu
