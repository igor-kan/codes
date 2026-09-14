#include <vector>
#include <string>
#include <functional>

class BloomFilter {
private:
    std::vector<bool> bit_array;
    int size;
    int hash_count;

    size_t hash_func(const std::string& item, int seed) {
        std::hash<std::string> hasher;
        return hasher(item + std::to_string(seed)) % size;
    }

public:
    BloomFilter(int size, int hash_count) : size(size), hash_count(hash_count) {
        bit_array.resize(size, false);
    }

    void add(const std::string& item) {
        for (int i = 0; i < hash_count; ++i) {
            bit_array[hash_func(item, i)] = true;
        }
    }

    bool check(const std::string& item) {
        for (int i = 0; i < hash_count; ++i) {
            if (!bit_array[hash_func(item, i)]) return false;
        }
        return true;
    }
};
