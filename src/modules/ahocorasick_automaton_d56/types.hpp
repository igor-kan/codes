#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_ahocorasick_automaton_d56 {
struct AcNode {
    int next[26];
    int fail = 0;
    int out_count = 0;
    AcNode() {
        for (int i = 0; i < 26; ++i) next[i] = -1;
    }
};

struct ModuleMeta {
    static constexpr const char* kSlug = "ahocorasick_automaton_d56";
    int version = 1;
};
} // namespace codes_ahocorasick_automaton_d56
