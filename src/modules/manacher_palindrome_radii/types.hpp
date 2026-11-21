#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_manacher_palindrome_radii {
struct PalindromeSpan {
    int start = 0;
    int length = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "manacher_palindrome_radii";
    int version = 1;
};
} // namespace codes_manacher_palindrome_radii
