// A Tour of C++ -- classes, constructors and methods.
#include <iostream>
#include <string>

class Shape {
  public:
    explicit Shape(std::string name) : name_(std::move(name)) {}
    virtual ~Shape() = default;
    virtual double area() const = 0;
    const std::string &name() const { return name_; }

  protected:
    std::string name_;
};

class Rectangle : public Shape {
  public:
    Rectangle(double w, double h) : Shape("rectangle"), w_(w), h_(h) {}
    double area() const override { return w_ * h_; }

  private:
    double w_, h_;
};

int main() {
    Rectangle r(3.0, 4.0);
    std::cout << r.name() << " area=" << r.area() << '\n';
    return 0;
}
