// Effective C++ -- Pimpl idiom to reduce compilation dependencies.
#include <iostream>
#include <memory>

class Widget {
  public:
    Widget();
    explicit Widget(int size);
    ~Widget();
    Widget(Widget &&) noexcept;
    Widget &operator=(Widget &&) noexcept;
    Widget(const Widget &);
    Widget &operator=(const Widget &);
    int size() const;

  private:
    struct Impl;
    std::unique_ptr<Impl> impl_;
};

struct Widget::Impl {
    int size;
};

Widget::Widget() : impl_(std::make_unique<Impl>(Impl{0})) {}
Widget::Widget(int size) : impl_(std::make_unique<Impl>(Impl{size})) {}
Widget::~Widget() = default;
Widget::Widget(Widget &&) noexcept = default;
Widget &Widget::operator=(Widget &&) noexcept = default;
Widget::Widget(const Widget &other) : impl_(std::make_unique<Impl>(*other.impl_)) {}
Widget &Widget::operator=(const Widget &other) {
    *impl_ = *other.impl_;
    return *this;
}
int Widget::size() const { return impl_->size; }

int main() {
    Widget widget(7);
    std::cout << "size=" << widget.size() << '\n';
    return 0;
}
