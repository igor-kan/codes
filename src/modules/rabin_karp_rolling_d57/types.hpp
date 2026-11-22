#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_rabin_karp_rolling_d57 {
struct HashWindowPair {
    long long h1 = 0;
    long long h2 = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "rabin_karp_rolling_d57";
    int version = 1;
};
} // namespace codes_rabin_karp_rolling_d57
