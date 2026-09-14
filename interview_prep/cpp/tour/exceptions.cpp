// A Tour of C++ -- exceptions and RAII-based unwinding.
#include <iostream>
#include <stdexcept>
#include <string>

class Guard {
  public:
    explicit Guard(std::string name) : name_(std::move(name)) {}
    ~Guard() { std::cout << "cleanup " << name_ << '\n'; }
  private:
    std::string name_;
};

int divide(int a, int b) {
    if (b == 0) throw std::invalid_argument("division by zero");
    return a / b;
}

int main() {
    Guard guard("scope");
    try {
        std::cout << divide(10, 2) << '\n';
        std::cout << divide(1, 0) << '\n';
    } catch (const std::invalid_argument &e) {
        std::cerr << "caught: " << e.what() << '\n';
    }
    return 0;
}
