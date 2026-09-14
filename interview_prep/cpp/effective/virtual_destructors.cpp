// Effective C++ -- virtual destructors for polymorphic bases.
#include <iostream>
#include <memory>

class Base {
  public:
    virtual ~Base() { std::cout << "~Base\n"; }
    virtual void run() const { std::cout << "Base::run\n"; }
};

class Derived : public Base {
  public:
    ~Derived() override { std::cout << "~Derived\n"; }
    void run() const override { std::cout << "Derived::run\n"; }
};

int main() {
    std::unique_ptr<Base> object = std::make_unique<Derived>();
    object->run();  // correct virtual dispatch and destruction
    return 0;
}
