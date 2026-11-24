#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_mos_distinct_freq_d59 {
struct PairRangeQ {
    int l = 0;
    int r = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "mos_distinct_freq_d59";
    int version = 1;
};
} // namespace codes_mos_distinct_freq_d59
