#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_pairing_heap_meldable {
struct PairingNode {
    std::int64_t key = 0;
    int payload = 0;
    int child = -1;
    int sibling = -1;
    int prev = -1;
    bool active = false;
};
} // namespace codes_pairing_heap_meldable
