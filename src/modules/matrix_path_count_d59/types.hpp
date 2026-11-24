#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_matrix_path_count_d59 {
struct WalkSpec {
    int vertices = 0;
    long long steps = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "matrix_path_count_d59";
    int version = 1;
};
} // namespace codes_matrix_path_count_d59
