#include "interface.hpp"
#include <cassert>
#include <cstdint>

int main() {
    using namespace codes_closest_pair_divide_conquer;
    uint64_t rng = 0xABCDEF12345ULL;
    auto unif = [&]() -> double {
        rng = rng * 6364136223846793005ULL + 1ULL;
        return static_cast<double>(rng & 0xFFFFF) / 1024.0;
    };
    std::vector<std::vector<Point2D>> clouds;
    for (int t = 0; t < 16; ++t) {
        std::vector<Point2D> c;
        for (int k = 0; k < 40; ++k) c.push_back({unif(), unif(), static_cast<std::size_t>(k)});
        clouds.push_back(std::move(c));
    }
    auto res = batch_closest_pairs(clouds);
    for (std::size_t i = 0; i < clouds.size(); ++i) {
        assert(verify_closest_pair_invariants(clouds[i], res[i]) == Status::Ok);
    }
    return 0;
}
