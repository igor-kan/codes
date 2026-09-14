// RAII joining thread: never leaves a joinable thread behind.
#include <iostream>
#include <thread>
#include <utility>

class joining_thread {
    std::thread t_;
  public:
    joining_thread() noexcept = default;
    template <typename Callable>
    explicit joining_thread(Callable &&fn) : t_(std::forward<Callable>(fn)) {}
    explicit joining_thread(std::thread t) noexcept : t_(std::move(t)) {}
    joining_thread(joining_thread &&other) noexcept : t_(std::move(other.t_)) {}
    joining_thread &operator=(joining_thread &&other) noexcept {
        if (joinable()) join();
        t_ = std::move(other.t_);
        return *this;
    }
    ~joining_thread() { if (joinable()) join(); }
    bool joinable() const noexcept { return t_.joinable(); }
    void join() { t_.join(); }
    void detach() { t_.detach(); }
    std::thread &as_thread() noexcept { return t_; }
};

int main() {
    joining_thread t([]{ std::cout << "joined on destruction\n"; });
    return 0;
}
