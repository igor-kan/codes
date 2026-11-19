#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_mo_tree_hilbert_order {
struct MoQuery {
    int l = 0;
    int r = 0;
    int id = 0;
    std::uint64_t h_ord = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "mo_tree_hilbert_order";
    int version = 1;
};
} // namespace codes_mo_tree_hilbert_order
