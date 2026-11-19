#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_stoer_wagner_global_mincut {
struct CutResult {
    std::int64_t weight = 0;
    int phases = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "stoer_wagner_global_mincut";
    int version = 1;
};
} // namespace codes_stoer_wagner_global_mincut
