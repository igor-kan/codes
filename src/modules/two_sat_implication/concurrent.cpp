#include "interface.hpp"
#include <thread>

namespace codes_two_sat_implication {
std::vector<SatResult> parallel_solve_instances(const std::vector<std::pair<int, std::vector<Clause2>>>& batch) {
    std::vector<SatResult> out(batch.size());
    std::size_t mid = batch.size() / 2;
    auto worker = [&](std::size_t lo, std::size_t hi) {
        for (std::size_t i = lo; i < hi; ++i) {
            TwoSatSolver s(batch[i].first);
            for (const auto& c : batch[i].second) s.add_or(c.var_a, c.neg_a, c.var_b, c.neg_b);
            out[i] = s.solve();
        }
    };
    std::thread t1(worker, 0, mid);
    std::thread t2(worker, mid, batch.size());
    t1.join();
    t2.join();
    return out;
}
} // namespace codes_two_sat_implication
