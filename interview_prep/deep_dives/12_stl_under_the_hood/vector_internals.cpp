// vector growth, capacity and iterator invalidation.
#include <iostream>
#include <vector>

int main() {
    std::vector<int> values;
    std::size_t last_capacity = 0;
    for (int i = 0; i < 20; ++i) {
        values.push_back(i);
        if (values.capacity() != last_capacity) {
            std::cout << "size=" << values.size()
                      << " capacity=" << values.capacity() << '\n';
            last_capacity = values.capacity();
        }
    }
    return 0;
}
