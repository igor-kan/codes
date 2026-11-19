#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_aho_kmp_failure_automaton {
struct DfaMatchSummary {
    int states = 0;
    std::int64_t matches = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "aho_kmp_failure_automaton";
    int version = 1;
};
} // namespace codes_aho_kmp_failure_automaton
