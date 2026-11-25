#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_li_chao_segment_d60 {
struct LinearFn {
    std::int64_t m;
    std::int64_t b;
    std::int64_t eval(std::int64_t x) const { return m * x + b; }
};

struct ModuleMeta {
    static constexpr const char* kSlug = "li_chao_segment_d60";
    int version = 1;
};
} // namespace codes_li_chao_segment_d60
