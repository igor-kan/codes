#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_suffix_automaton_lcs {
struct SamState {
    int len = 0;
    int link = -1;
    int next[26];
    SamState() { std::fill(std::begin(next), std::end(next), -1); }
};

struct ModuleMeta {
    static constexpr const char* kSlug = "suffix_automaton_lcs";
    int version = 1;
};
} // namespace codes_suffix_automaton_lcs
