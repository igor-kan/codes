#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_aho_corasick_dfa_d60 {
struct AcNode {
    int next[26];
    int fail;
    int out_cnt;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "aho_corasick_dfa_d60";
    int version = 1;
};
} // namespace codes_aho_corasick_dfa_d60
