// shared_ptr: reference counting and use_count.
#include <iostream>
#include <memory>
#include <vector>

int main() {
    auto shared = std::make_shared<int>(42);
    std::cout << "count=" << shared.use_count() << '\n';
    {
        std::vector<std::shared_ptr<int>> owners{shared, shared};
        std::cout << "count inside=" << shared.use_count() << '\n';
    }
    std::cout << "count after=" << shared.use_count()
              << " value=" << *shared << '\n';
    return 0;
}
