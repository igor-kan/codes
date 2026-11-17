#include "interface.hpp"

namespace codes_pairing_heap_meldable {
void verify_pairing_heap_order(const PairingHeap& h) {
    const auto& raw = h.raw_nodes();
    for (std::size_t i = 0; i < raw.size(); ++i) {
        if (!raw[i].active) continue;
        int c = raw[i].child;
        while (c != -1) {
            if (raw[static_cast<std::size_t>(c)].key < raw[i].key) {
                throw std::logic_error("pairing heap parent > child");
            }
            c = raw[static_cast<std::size_t>(c)].sibling;
        }
    }
}
} // namespace codes_pairing_heap_meldable
