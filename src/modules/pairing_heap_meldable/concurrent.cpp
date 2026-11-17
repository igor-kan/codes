#include "interface.hpp"
#include <thread>

namespace codes_pairing_heap_meldable {
std::vector<std::vector<std::int64_t>> parallel_sort_chunks(const std::vector<std::vector<std::int64_t>>& chunks) {
    std::vector<std::vector<std::int64_t>> out(chunks.size());
    std::size_t mid = chunks.size() / 2;
    auto worker = [&](std::size_t lo, std::size_t hi) {
        for (std::size_t i = lo; i < hi; ++i) out[i] = fast_heapsort_pairing(chunks[i]);
    };
    std::thread t1(worker, 0, mid);
    std::thread t2(worker, mid, chunks.size());
    t1.join();
    t2.join();
    return out;
}
} // namespace codes_pairing_heap_meldable
