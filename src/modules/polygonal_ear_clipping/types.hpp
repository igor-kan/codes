#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_polygonal_ear_clipping {
struct Vec2 { double x = 0.0; double y = 0.0; };
struct TriIdx { int a; int b; int c; };

struct ModuleMeta {
    static constexpr const char* kSlug = "polygonal_ear_clipping";
    int version = 1;
};
} // namespace codes_polygonal_ear_clipping
