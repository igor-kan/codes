#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    std::size_t sink = 0;
    std::vector<int> a(512); for(int i=0;i<512;++i) a[i]=i%23; std::vector<codes_mo_offline_queries::RangeQuery> q; for(std::size_t i=0;i<200;++i) q.push_back({i%200, i%200+250, i});
    auto t0 = std::chrono::steady_clock::now();
    for (int it = 0; it < 200; ++it) {
        sink += codes_mo_offline_queries::answer_distinct_queries(a, q).size();
    }
    auto t1 = std::chrono::steady_clock::now();
    double ns = std::chrono::duration<double, std::nano>(t1 - t0).count() / 200.0;
    std::cout << "mo_offline_queries ns=" << ns << " sink=" << sink << "\n";
    return 0;
}
