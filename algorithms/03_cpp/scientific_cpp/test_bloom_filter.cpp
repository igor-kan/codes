#include <iostream>
#include <cassert>
#include "bloom_filter.hpp"

int main() {
    BloomFilter bf(1024);
    bf.insert("quantum");
    bf.insert("gravity");
    assert(bf.contains("quantum"));
    assert(bf.contains("gravity"));
    assert(!bf.contains("nonexistent_element"));
    std::cout << "test_bloom_filter PASSED\n";
    return 0;
}
