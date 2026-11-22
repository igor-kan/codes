#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_lis_patience_sort_d57 {
struct LisSummary {
    int length = 0;
    long long last_tail = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "lis_patience_sort_d57";
    int version = 1;
};
} // namespace codes_lis_patience_sort_d57
