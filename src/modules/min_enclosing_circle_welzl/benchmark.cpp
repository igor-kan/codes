#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_min_enclosing_circle_welzl;
    std::vector<Point2D> pts = {{0,0},{4,0},{0,4},{2,1}};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += static_cast<std::int64_t>(minimum_enclosing_disk(pts).r * 1000);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "min_enclosing_circle_welzl us=" << us << " sink=" << sink << "\n";
    return 0;
}
