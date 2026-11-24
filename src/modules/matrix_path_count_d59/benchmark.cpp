#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_matrix_path_count_d59;
    std::vector<std::vector<long long>> b_adj = {{1,1,0},{0,1,1},{1,0,1}};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += count_k_walks(b_adj, 5)[0][2];
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "matrix_path_count_d59 us=" << us << " sink=" << sink << "\n";
    return 0;
}
