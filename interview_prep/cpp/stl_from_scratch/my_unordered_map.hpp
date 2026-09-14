// Minimal chained hash map.
#pragma once
#include <cstddef>
#include <functional>
#include <utility>
#include <vector>

namespace mystl {

template <typename K, typename V, typename Hash = std::hash<K>>
class unordered_map {
    struct node {
        K key;
        V value;
        node *next;
    };

  public:
    explicit unordered_map(std::size_t buckets = 8) : buckets_(buckets, nullptr) {}
    ~unordered_map() { clear(); }
    unordered_map(const unordered_map &) = delete;
    unordered_map &operator=(const unordered_map &) = delete;

    void insert(const K &key, const V &value) {
        if (size_ + 1 > buckets_.size()) rehash(buckets_.size() * 2);
        std::size_t index = Hash{}(key) % buckets_.size();
        for (node *n = buckets_[index]; n; n = n->next)
            if (n->key == key) { n->value = value; return; }
        buckets_[index] = new node{key, value, buckets_[index]};
        ++size_;
    }

    V *find(const K &key) {
        for (node *n = buckets_[Hash{}(key) % buckets_.size()]; n; n = n->next)
            if (n->key == key) return &n->value;
        return nullptr;
    }

    std::size_t size() const noexcept { return size_; }
    void clear() {
        for (node *&head : buckets_) { while (head) { node *next = head->next; delete head; head = next; } }
        size_ = 0;
    }

  private:
    void rehash(std::size_t count) {
        std::vector<node *> fresh(count, nullptr);
        for (node *head : buckets_)
            while (head) {
                node *next = head->next;
                std::size_t index = Hash{}(head->key) % count;
                head->next = fresh[index];
                fresh[index] = head;
                head = next;
            }
        buckets_.swap(fresh);
    }

    std::vector<node *> buckets_;
    std::size_t size_ = 0;
};

}  // namespace mystl
