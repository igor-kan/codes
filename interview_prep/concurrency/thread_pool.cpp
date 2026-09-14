// A fixed-size thread pool with a task queue.
#include <condition_variable>
#include <functional>
#include <future>
#include <iostream>
#include <memory>
#include <mutex>
#include <queue>
#include <thread>
#include <type_traits>
#include <vector>

class thread_pool {
    std::vector<std::thread> workers_;
    std::queue<std::function<void()>> tasks_;
    std::mutex mtx_;
    std::condition_variable cv_;
    bool stop_ = false;
  public:
    explicit thread_pool(unsigned threads = std::thread::hardware_concurrency()) {
        for (unsigned i = 0; i < threads; ++i)
            workers_.emplace_back([this] {
                for (;;) {
                    std::function<void()> task;
                    {
                        std::unique_lock<std::mutex> lock(mtx_);
                        cv_.wait(lock, [this]{ return stop_ || !tasks_.empty(); });
                        if (stop_ && tasks_.empty()) return;
                        task = std::move(tasks_.front());
                        tasks_.pop();
                    }
                    task();
                }
            });
    }
    ~thread_pool() {
        { std::lock_guard<std::mutex> lock(mtx_); stop_ = true; }
        cv_.notify_all();
        for (auto &t : workers_) t.join();
    }
    template <typename F, typename... Args>
    auto submit(F &&fn, Args &&...args) -> std::future<std::invoke_result_t<F, Args...>> {
        using result = std::invoke_result_t<F, Args...>;
        auto task = std::make_shared<std::packaged_task<result()>>(
            [fn = std::forward<F>(fn), ...a = std::forward<Args>(args)]() mutable { return fn(a...); });
        std::future<result> future = task->get_future();
        { std::lock_guard<std::mutex> lock(mtx_); tasks_.emplace([task]{ (*task)(); }); }
        cv_.notify_one();
        return future;
    }
};

int main() {
    thread_pool pool(4);
    auto a = pool.submit([]{ return 20 + 22; });
    auto b = pool.submit([](int n){ return n * n; }, 5);
    std::cout << a.get() << ' ' << b.get() << '\n';
    return 0;
}
