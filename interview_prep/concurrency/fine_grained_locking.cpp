// Fine-grained locking with a per-bucket mutex hash map.
#include <iostream>
#include <list>
#include <mutex>
#include <string>
#include <vector>

template <typename K, typename V>
class bucket_map {
    struct bucket {
        std::list<std::pair<K, V>> entries;
        std::mutex mtx;
    };
    std::vector<bucket> buckets_;
    std::hash<K> hasher_;

    bucket &get(const K &key) { return buckets_[hasher_(key) % buckets_.size()]; }

  public:
    explicit bucket_map(std::size_t n) : buckets_(n) {}

    void insert(const K &key, const V &value) {
        auto &b = get(key);
        std::lock_guard<std::mutex> lock(b.mtx);
        b.entries.emplace_back(key, value);
    }
    bool find(const K &key, V &out) {
        auto &b = get(key);
        std::lock_guard<std::mutex> lock(b.mtx);
        for (auto &[k, v] : b.entries)
            if (k == key) { out = v; return true; }
        return false;
    }
};

int main() {
    bucket_map<std::string, int> map(16);
    map.insert("one", 1);
    int value = 0;
    bool found = map.find("one", value);
    std::cout << found << ' ' << value << '\n';
    return found && value == 1 ? 0 : 1;
}
