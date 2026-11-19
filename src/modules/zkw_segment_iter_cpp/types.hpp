#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_zkw_segment_iter_cpp {
struct ZkwCfg {
    int leaf_base = 1;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "zkw_segment_iter_cpp";
    int version = 1;
};
} // namespace codes_zkw_segment_iter_cpp
