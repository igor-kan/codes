#include "bloom_filter.hpp"

BloomFilter::BloomFilter(size_t bit_size) : bits_(bit_size, false), size_(bit_size) {}

static size_t hash1(const std::string& s) {
    size_t h = 5381;
    for (char c : s) h = ((h << 5) + h) + c;
    return h;
}

static size_t hash2(const std::string& s) {
    size_t h = 0;
    for (char c : s) h = c + (h << 6) + (h << 16) - h;
    return h;
}

void BloomFilter::insert(const std::string& key) {
    bits_[hash1(key) % size_] = true;
    bits_[hash2(key) % size_] = true;
}

bool BloomFilter::contains(const std::string& key) const {
    return bits_[hash1(key) % size_] && bits_[hash2(key) % size_];
}
