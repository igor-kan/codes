#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_pairing_heap_meldable;
    PairingHeap h;
    int h1 = h.push(50, 1);
    int h2 = h.push(30, 2);
    int h3 = h.push(40, 3);
    verify_pairing_heap_order(h);
    h.decrease_key(h1, 10);
    verify_pairing_heap_order(h);
    assert(h.pop_min().first == 10);
    h.decrease_key(h3, 25);
    assert(h.pop_min().first == 25);
    assert(h.pop_min().first == 30);
    assert(h.empty());
    (void)h2;
    return 0;
}
