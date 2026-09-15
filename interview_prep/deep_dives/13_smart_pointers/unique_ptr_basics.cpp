// unique_ptr: single ownership and transfer.
#include <iostream>
#include <memory>

struct Resource {
    int id;
    explicit Resource(int i) : id(i) { std::cout << "acquire " << id << '\n'; }
    ~Resource() { std::cout << "release " << id << '\n'; }
};

std::unique_ptr<Resource> make(int id) { return std::make_unique<Resource>(id); }

int main() {
    auto owner = make(1);
    auto moved = std::move(owner);
    std::cout << (owner == nullptr) << ' ' << moved->id << '\n';
    return 0;
}
