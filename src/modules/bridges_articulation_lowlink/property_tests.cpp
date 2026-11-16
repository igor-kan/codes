#include "interface.hpp"
#include <cassert>
#include <cstdint>

int main() {
    using namespace codes_bridges_articulation_lowlink;
    uint64_t rng = 0xCAFEBABE12345678ULL;
    auto nxt = [&]() -> uint64_t {
        rng = rng * 6364136223846793005ULL + 1442695040888963407ULL;
        return rng >> 32;
    };
    std::vector<std::pair<std::size_t, std::vector<UndirectedEdge>>> batch;
    for (int t = 0; t < 20; ++t) {
        std::size_t n = 8 + (t % 7);
        std::vector<UndirectedEdge> e;
        std::size_t m = n + (nxt() % (n * 2));
        for (std::size_t j = 0; j < m; ++j) {
            e.push_back({static_cast<std::size_t>(nxt() % n), static_cast<std::size_t>(nxt() % n)});
        }
        batch.push_back({n, std::move(e)});
    }
    auto res = batch_cut_reports(batch);
    for (std::size_t i = 0; i < batch.size(); ++i) {
        auto r_rec = find_bridges_and_articulations(batch[i].first, batch[i].second);
        assert(res[i].bridge_edge_ids == r_rec.bridge_edge_ids);
        assert(res[i].articulation_vertices == r_rec.articulation_vertices);
        assert(verify_cut_oracle(batch[i].first, batch[i].second, res[i]) == Status::Ok);
    }
    return 0;
}
