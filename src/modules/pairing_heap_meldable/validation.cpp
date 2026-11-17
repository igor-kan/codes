#include "interface.hpp"

namespace codes_pairing_heap_meldable {
void validate_handle(const PairingHeap& h, int handle) {
    const auto& n = h.raw_nodes();
    if (handle < 0 || handle >= static_cast<int>(n.size()) || !n[static_cast<std::size_t>(handle)].active) {
        throw std::out_of_range("invalid or inactive pairing heap handle");
    }
}
} // namespace codes_pairing_heap_meldable
