#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_prim_dense_mst_d58 {
struct DenseMstStats {
    long long weight = 0;
    int vertices = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "prim_dense_mst_d58";
    int version = 1;
};
} // namespace codes_prim_dense_mst_d58
