// Cross-module integration & throughput driver for Day 55 `codes` modules.
#include "../src/modules/stoer_wagner_global_mincut/interface.hpp"
#include "../src/modules/zkw_segment_iter_cpp/interface.hpp"
#include "../src/modules/mo_tree_hilbert_order/interface.hpp"
#include "../src/modules/pollard_rho_brent_u128/interface.hpp"
#include "../src/modules/aho_kmp_failure_automaton/interface.hpp"
#include <chrono>
#include <cstdint>
#include <iostream>

int main() {
    auto t0 = std::chrono::steady_clock::now();
    std::int64_t sink = 0;
    codes_stoer_wagner_global_mincut::validate_problem_size(8); sink += codes_stoer_wagner_global_mincut::fast_checksum_span({1, 2, 3, 1});
    codes_zkw_segment_iter_cpp::validate_problem_size(8); sink += codes_zkw_segment_iter_cpp::fast_checksum_span({1, 2, 3, 2});
    codes_mo_tree_hilbert_order::validate_problem_size(8); sink += codes_mo_tree_hilbert_order::fast_checksum_span({1, 2, 3, 3});
    codes_pollard_rho_brent_u128::validate_problem_size(8); sink += codes_pollard_rho_brent_u128::fast_checksum_span({1, 2, 3, 4});
    codes_aho_kmp_failure_automaton::validate_problem_size(8); sink += codes_aho_kmp_failure_automaton::fast_checksum_span({1, 2, 3, 5});
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "codes day55 cross-module suite us=" << us << " sink=" << sink << "\n";
    return sink != 0 ? 0 : 1;
}
