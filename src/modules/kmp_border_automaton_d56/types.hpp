#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_kmp_border_automaton_d56 {
struct KmpStats {
    std::size_t pattern_len = 0;
    int max_border = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "kmp_border_automaton_d56";
    int version = 1;
};
} // namespace codes_kmp_border_automaton_d56
