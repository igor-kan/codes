#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_min_enclosing_circle_welzl {
struct Point2D { double x = 0.0; double y = 0.0; };
struct Disk2D { double cx = 0.0; double cy = 0.0; double r = 0.0; };

struct ModuleMeta {
    static constexpr const char* kSlug = "min_enclosing_circle_welzl";
    int version = 1;
};
} // namespace codes_min_enclosing_circle_welzl
