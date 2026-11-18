#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_persistent_treap_split {
struct PTreapNode {
    std::int64_t val = 0;
    std::int64_t sum = 0;
    std::uint32_t prio = 0;
    int sz = 1;
    int l = -1;
    int r = -1;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "persistent_treap_split";
    int version = 1;
};
} // namespace codes_persistent_treap_split
