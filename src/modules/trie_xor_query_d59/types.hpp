#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_trie_xor_query_d59 {
struct XorNode {
    int child[2] = {-1, -1};
};

struct ModuleMeta {
    static constexpr const char* kSlug = "trie_xor_query_d59";
    int version = 1;
};
} // namespace codes_trie_xor_query_d59
