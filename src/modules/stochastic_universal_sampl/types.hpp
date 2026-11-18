#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_stochastic_universal_sampl {
struct AliasBucket {
    double prob = 1.0;
    int alias = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "stochastic_universal_sampl";
    int version = 1;
};
} // namespace codes_stochastic_universal_sampl
