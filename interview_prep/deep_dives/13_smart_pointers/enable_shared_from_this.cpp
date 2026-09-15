// enable_shared_from_this gives an object a shared_ptr to itself safely.
#include <iostream>
#include <memory>

class Session : public std::enable_shared_from_this<Session> {
  public:
    std::shared_ptr<Session> self() { return shared_from_this(); }
    ~Session() { std::cout << "Session destroyed\n"; }
};

int main() {
    auto session = std::make_shared<Session>();
    auto also = session->self();
    std::cout << "use_count=" << session.use_count() << '\n';
    return 0;
}
