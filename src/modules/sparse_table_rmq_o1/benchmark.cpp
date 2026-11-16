#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    std::size_t sink = 0;
    std::vector<int64_t> v(1024); for(std::size_t i=0;i<1024;++i) v[i]=static_cast<int64_t>((i*41)%503); auto tab = codes_sparse_table_rmq_o1::build_sparse_table(v);
    auto t0 = std::chrono::steady_clock::now();
    for (int it = 0; it < 200; ++it) {
        for(std::size_t q=0;q<50;++q) sink += static_cast<std::size_t>(codes_sparse_table_rmq_o1::query_rmq_o1(tab, q*7, q*7+300));
    }
    auto t1 = std::chrono::steady_clock::now();
    double ns = std::chrono::duration<double, std::nano>(t1 - t0).count() / 200.0;
    std::cout << "sparse_table_rmq_o1 ns=" << ns << " sink=" << sink << "\n";
    return 0;
}
