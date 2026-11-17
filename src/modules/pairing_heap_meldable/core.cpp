#include "interface.hpp"

namespace codes_pairing_heap_meldable {

int PairingHeap::meld(int a, int b) {
    if (a == -1) return b;
    if (b == -1) return a;
    if (nodes_[static_cast<std::size_t>(a)].key > nodes_[static_cast<std::size_t>(b)].key) std::swap(a, b);
    nodes_[static_cast<std::size_t>(b)].prev = a;
    nodes_[static_cast<std::size_t>(b)].sibling = nodes_[static_cast<std::size_t>(a)].child;
    if (nodes_[static_cast<std::size_t>(a)].child != -1) {
        nodes_[static_cast<std::size_t>(nodes_[static_cast<std::size_t>(a)].child)].prev = b;
    }
    nodes_[static_cast<std::size_t>(a)].child = b;
    nodes_[static_cast<std::size_t>(a)].prev = -1;
    nodes_[static_cast<std::size_t>(a)].sibling = -1;
    return a;
}

int PairingHeap::two_pass_merge(int first) {
    if (first == -1) return -1;
    std::vector<int> pairs;
    int cur = first;
    while (cur != -1) {
        int a = cur;
        int b = nodes_[static_cast<std::size_t>(a)].sibling;
        int next = (b != -1) ? nodes_[static_cast<std::size_t>(b)].sibling : -1;
        nodes_[static_cast<std::size_t>(a)].sibling = -1;
        nodes_[static_cast<std::size_t>(a)].prev = -1;
        if (b != -1) {
            nodes_[static_cast<std::size_t>(b)].sibling = -1;
            nodes_[static_cast<std::size_t>(b)].prev = -1;
            pairs.push_back(meld(a, b));
        } else {
            pairs.push_back(a);
        }
        cur = next;
    }
    int acc = -1;
    for (int i = static_cast<int>(pairs.size()) - 1; i >= 0; --i) {
        acc = meld(acc, pairs[static_cast<std::size_t>(i)]);
    }
    return acc;
}

int PairingHeap::push(std::int64_t key, int payload) {
    int id = static_cast<int>(nodes_.size());
    nodes_.push_back({key, payload, -1, -1, -1, true});
    root_ = meld(root_, id);
    ++count_;
    return id;
}

void PairingHeap::decrease_key(int handle, std::int64_t new_key) {
    validate_handle(*this, handle);
    auto& node = nodes_[static_cast<std::size_t>(handle)];
    if (new_key > node.key) throw std::invalid_argument("new_key exceeds current key");
    node.key = new_key;
    if (handle == root_) return;
    int p = node.prev;
    if (nodes_[static_cast<std::size_t>(p)].child == handle) {
        nodes_[static_cast<std::size_t>(p)].child = node.sibling;
    } else {
        nodes_[static_cast<std::size_t>(p)].sibling = node.sibling;
    }
    if (node.sibling != -1) {
        nodes_[static_cast<std::size_t>(node.sibling)].prev = p;
    }
    node.prev = -1;
    node.sibling = -1;
    root_ = meld(root_, handle);
}

std::pair<std::int64_t, int> PairingHeap::pop_min() {
    if (root_ == -1) throw std::runtime_error("heap is empty");
    int old = root_;
    std::pair<std::int64_t, int> res{nodes_[static_cast<std::size_t>(old)].key,
                                    nodes_[static_cast<std::size_t>(old)].payload};
    nodes_[static_cast<std::size_t>(old)].active = false;
    int children = nodes_[static_cast<std::size_t>(old)].child;
    nodes_[static_cast<std::size_t>(old)].child = -1;
    root_ = two_pass_merge(children);
    --count_;
    return res;
}

std::int64_t PairingHeap::min_key() const {
    if (root_ == -1) throw std::runtime_error("heap is empty");
    return nodes_[static_cast<std::size_t>(root_)].key;
}

} // namespace codes_pairing_heap_meldable
