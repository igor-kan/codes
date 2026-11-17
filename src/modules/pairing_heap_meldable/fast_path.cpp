#include "interface.hpp"

namespace codes_pairing_heap_meldable {
std::vector<std::int64_t> fast_heapsort_pairing(const std::vector<std::int64_t>& vals) {
    PairingHeap h;
    for (std::size_t i = 0; i < vals.size(); ++i) h.push(vals[i], static_cast<int>(i));
    std::vector<std::int64_t> out;
    out.reserve(vals.size());
    while (!h.empty()) out.push_back(h.pop_min().first);
    return out;
}
} // namespace codes_pairing_heap_meldable
