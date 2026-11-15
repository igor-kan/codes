#include "interface.hpp"
#include <thread>

namespace codes_z_algorithm_lcp {
std::vector<std::vector<std::size_t>> batch_find_matches(const std::vector<std::string>& texts, const std::string& pat) {
    std::vector<std::vector<std::size_t>> out(texts.size());
    std::vector<std::thread> workers;
    const std::size_t nt = std::min<std::size_t>(4, texts.size());
    for (std::size_t t = 0; t < nt; ++t) {
        workers.emplace_back([&, t]() {
            for (std::size_t i = t; i < texts.size(); i += nt) {
                out[i] = find_matches(texts[i], pat);
            }
        });
    }
    for (auto& w : workers) w.join();
    return out;
}
} // namespace codes_z_algorithm_lcp
