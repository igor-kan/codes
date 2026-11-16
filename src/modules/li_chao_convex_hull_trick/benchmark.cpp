#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    std::size_t sink = 0;
    auto t = codes_li_chao_convex_hull_trick::make_lichao_tree(-10000, 10000); for(int64_t k=-50;k<=50;++k) codes_li_chao_convex_hull_trick::insert_line(t, {k, k*k});
    auto t0 = std::chrono::steady_clock::now();
    for (int it = 0; it < 200; ++it) {
        for(int64_t x=-100;x<100;++x) sink += static_cast<std::size_t>(codes_li_chao_convex_hull_trick::query_min_fast(t, x));
    }
    auto t1 = std::chrono::steady_clock::now();
    double ns = std::chrono::duration<double, std::nano>(t1 - t0).count() / 200.0;
    std::cout << "li_chao_convex_hull_trick ns=" << ns << " sink=" << sink << "\n";
    return 0;
}
