#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_sliding_window_deque_extrema {
struct WindowExtremum {
    long long min_val = 0;
    long long max_val = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "sliding_window_deque_extrema";
    int version = 1;
};
} // namespace codes_sliding_window_deque_extrema
