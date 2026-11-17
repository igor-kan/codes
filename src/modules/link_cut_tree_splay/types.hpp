#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_link_cut_tree_splay {
struct LctNode {
    int parent = -1;
    int ch[2] = {-1, -1};
    bool rev = false;
    std::int64_t val = 0;
    std::int64_t sum = 0;
    std::int64_t max_val = 0;
};
} // namespace codes_link_cut_tree_splay
