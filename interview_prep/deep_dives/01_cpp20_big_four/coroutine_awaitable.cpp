// A custom awaitable that suspends and resumes.
#include <coroutine>
#include <iostream>

struct Resumable {
    bool await_ready() const noexcept {
        std::cout << "await_ready\n";
        return false;
    }
    void await_suspend(std::coroutine_handle<> handle) const {
        std::cout << "await_suspend (would resume later)\n";
        handle.resume();  // resume immediately for the demo
    }
    void await_resume() const noexcept { std::cout << "await_resume\n"; }
};

struct Demo {
    struct promise_type {
        Demo get_return_object() { return {}; }
        std::suspend_never initial_suspend() noexcept { return {}; }
        std::suspend_never final_suspend() noexcept { return {}; }
        void return_void() {}
        void unhandled_exception() { std::terminate(); }
    };
};

Demo run() {
    std::cout << "before co_await\n";
    co_await Resumable{};
    std::cout << "after co_await\n";
}

int main() {
    run();
    return 0;
}
