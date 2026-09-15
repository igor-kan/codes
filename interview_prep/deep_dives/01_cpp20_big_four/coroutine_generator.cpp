// A generator coroutine producing a lazy sequence.
#include <coroutine>
#include <iostream>
#include <optional>
#include <utility>

template <typename T>
class Generator {
  public:
    struct promise_type {
        T current;
        Generator get_return_object() {
            return Generator{std::coroutine_handle<promise_type>::from_promise(*this)};
        }
        std::suspend_always initial_suspend() noexcept { return {}; }
        std::suspend_always final_suspend() noexcept { return {}; }
        std::suspend_always yield_value(T value) {
            current = value;
            return {};
        }
        void return_void() {}
        void unhandled_exception() { std::terminate(); }
    };

    explicit Generator(std::coroutine_handle<promise_type> handle) : handle_(handle) {}
    ~Generator() { if (handle_) handle_.destroy(); }
    Generator(const Generator &) = delete;
    Generator(Generator &&other) noexcept : handle_(std::exchange(other.handle_, {})) {}

    bool next() {
        handle_.resume();
        return !handle_.done();
    }
    T value() const { return handle_.promise().current; }

  private:
    std::coroutine_handle<promise_type> handle_;
};

Generator<int> range(int start, int stop, int step = 1) {
    for (int value = start; value < stop; value += step) co_yield value;
}

int main() {
    auto gen = range(0, 10, 2);
    while (gen.next()) std::cout << gen.value() << ' ';
    std::cout << '\n';
    return 0;
}
