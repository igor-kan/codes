#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_pairing_heap_meldable {
class PairingHeap {
public:
    int push(std::int64_t key, int payload);
    void decrease_key(int handle, std::int64_t new_key);
    std::pair<std::int64_t, int> pop_min();
    std::int64_t min_key() const;
    bool empty() const { return root_ == -1; }
    int size() const { return count_; }
    const std::vector<PairingNode>& raw_nodes() const { return nodes_; }

private:
    std::vector<PairingNode> nodes_;
    int root_ = -1;
    int count_ = 0;
    int meld(int a, int b);
    int two_pass_merge(int first);
};

void validate_handle(const PairingHeap& h, int handle);
std::vector<std::int64_t> fast_heapsort_pairing(const std::vector<std::int64_t>& vals);
std::vector<std::vector<std::int64_t>> parallel_sort_chunks(const std::vector<std::vector<std::int64_t>>& chunks);
void verify_pairing_heap_order(const PairingHeap& h);
} // namespace codes_pairing_heap_meldable
