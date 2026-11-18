#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_polygonal_ear_clipping;
    std::vector<Vec2> p = {{0,0},{4,0},{4,3},{2,1.5},{0,3}};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += static_cast<std::int64_t>(ear_clip_triangulate(p).size());
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "polygonal_ear_clipping us=" << us << " sink=" << sink << "\n";
    return 0;
}
