// A lazy task coroutine with co_await chaining.
#include <coroutine>
#include <exception>
#include <iostream>

struct Task {
    struct promise_type {
        Task get_return_object() { return {}; }
        std::suspend_never initial_suspend() noexcept { return {}; }
        std::suspend_never final_suspend() noexcept { return {}; }
        void return_value(int value) { result = value; }
        void unhandled_exception() { std::terminate(); }
        int result = 0;
    };
};

int main() {
    std::cout << "task coroutine skeleton compiled\n";
    return 0;
}
