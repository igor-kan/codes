#ifndef BLOOM_FILTER_HPP
#define BLOOM_FILTER_HPP

#include <vector>
#include <string>

class BloomFilter {
public:
    BloomFilter(size_t bit_size);
    void insert(const std::string& key);
    bool contains(const std::string& key) const;
private:
    std::vector<bool> bits_;
    size_t size_;
};

#endif
