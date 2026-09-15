// Allocator-aware containers and stateful allocators.
#include <iostream>
#include <memory>
#include <vector>

template <typename T>
struct CountingAllocator {
    using value_type = T;
    int *allocations;

    explicit CountingAllocator(int *count) : allocations(count) {}
    template <typename U>
    CountingAllocator(const CountingAllocator<U> &other) : allocations(other.allocations) {}

    T *allocate(std::size_t n) {
        ++*allocations;
        return static_cast<T *>(::operator new(n * sizeof(T)));
    }
    void deallocate(T *p, std::size_t) { ::operator delete(p); }

    template <typename U>
    bool operator==(const CountingAllocator<U> &other) const { return allocations == other.allocations; }
};

int main() {
    int allocations = 0;
    std::vector<int, CountingAllocator<int>> values{CountingAllocator<int>(&allocations)};
    for (int i = 0; i < 100; ++i) values.push_back(i);
    std::cout << "allocations=" << allocations << " size=" << values.size() << '\n';
    return 0;
}
