/**
 * Thread-Safe Generic LRU Cache using STL list and unordered_map.
 * 
 * Why C++ for this module?
 * C++ RAII, templates, and fine-grained mutex concurrency provide zero-overhead
 * generic abstractions essential for production database cache tiers.
 */

#pragma once

#include <list>
#include <unordered_map>
#include <mutex>
#include <optional>
#include <cassert>
#include <iostream>

template <typename K, typename V>
class LRUCache {
public:
    explicit LRUCache(size_t capacity) : capacity_(capacity) {
        assert(capacity > 0);
    }

    std::optional<V> get(const K& key) {
        std::lock_guard<std::mutex> lock(mutex_);
        auto it = index_.find(key);
        if (it == index_.end()) {
            return std::nullopt;
        }
        // Move accessed node to front (most recently used)
        items_.splice(items_.begin(), items_, it->second);
        return it->second->second;
    }

    void put(const K& key, const V& value) {
        std::lock_guard<std::mutex> lock(mutex_);
        auto it = index_.find(key);
        if (it != index_.end()) {
            // Update value and move to front
            it->second->second = value;
            items_.splice(items_.begin(), items_, it->second);
            return;
        }

        // Evict least recently used if at capacity
        if (items_.size() >= capacity_) {
            auto lru = items_.back();
            index_.erase(lru.first);
            items_.pop_back();
        }

        items_.emplace_front(key, value);
        index_[key] = items_.begin();
    }

    size_t size() const {
        std::lock_guard<std::mutex> lock(mutex_);
        return items_.size();
    }

private:
    using Node = std::pair<K, V>;
    size_t capacity_;
    std::list<Node> items_;
    std::unordered_map<K, typename std::list<Node>::iterator> index_;
    mutable std::mutex mutex_;
};

#ifdef COMPILE_TEST_MAIN
int main() {
    LRUCache<int, std::string> cache(2);
    cache.put(1, "one");
    cache.put(2, "two");
    assert(cache.get(1).value() == "one");
    cache.put(3, "three"); // evicts 2
    assert(!cache.get(2).has_value());
    assert(cache.get(3).value() == "three");
    std::cout << "C++ LRU Cache verification passed." << std::endl;
    return 0;
}
#endif
