// make_shared allocates the control block together with the object.
#include <iostream>
#include <memory>

struct Payload {
    int value;
    explicit Payload(int v) : value(v) { std::cout << "Payload ctor\n"; }
    ~Payload() { std::cout << "Payload dtor\n"; }
};

int main() {
    std::shared_ptr<Payload> combined = std::make_shared<Payload>(1);
    std::shared_ptr<Payload> separate(new Payload(2));  // two allocations

    std::weak_ptr<Payload> observer = combined;
    std::cout << "combined count=" << combined.use_count()
              << " weak live=" << !observer.expired() << '\n';
    return 0;
}
