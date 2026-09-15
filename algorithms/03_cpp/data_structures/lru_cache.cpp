// LRU cache with a list + hash map.
#include <cassert>
#include <iostream>
#include <list>
#include <unordered_map>

class LRUCache {
  public:
    explicit LRUCache(int capacity) : capacity_(capacity) {}

    int get(int key) {
        auto it = index_.find(key);
        if (it == index_.end()) return -1;
        items_.splice(items_.begin(), items_, it->second);
        return it->second->second;
    }

    void put(int key, int value) {
        auto it = index_.find(key);
        if (it != index_.end()) {
            it->second->second = value;
            items_.splice(items_.begin(), items_, it->second);
            return;
        }
        if (static_cast<int>(items_.size()) == capacity_) {
            index_.erase(items_.back().first);
            items_.pop_back();
        }
        items_.emplace_front(key, value);
        index_[key] = items_.begin();
    }

  private:
    int capacity_;
    std::list<std::pair<int, int>> items_;
    std::unordered_map<int, std::list<std::pair<int, int>>::iterator> index_;
};

int main() {
    LRUCache cache(2);
    cache.put(1, 1);
    cache.put(2, 2);
    assert(cache.get(1) == 1);
    cache.put(3, 3);
    assert(cache.get(2) == -1);
    std::cout << "lru cache ok\n";
    return 0;
}
