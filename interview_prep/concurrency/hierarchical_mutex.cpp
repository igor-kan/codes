// Hierarchical mutex to enforce lock ordering (C++ Concurrency in Action).
#include <climits>
#include <iostream>
#include <mutex>
#include <stdexcept>
#include <thread>

class hierarchical_mutex {
    std::mutex internal_;
    unsigned long const hierarchy_value_;
    unsigned long previous_hierarchy_ = 0;
    static inline thread_local unsigned long this_thread_hierarchy_ = ULONG_MAX;

    void check_for_hierarchy_violation() {
        if (this_thread_hierarchy_ <= hierarchy_value_)
            throw std::logic_error("mutex hierarchy violated");
    }
    void update_hierarchy_value() {
        previous_hierarchy_ = this_thread_hierarchy_;
        this_thread_hierarchy_ = hierarchy_value_;
    }

  public:
    explicit hierarchical_mutex(unsigned long value) : hierarchy_value_(value) {}

    void lock() {
        check_for_hierarchy_violation();
        internal_.lock();
        update_hierarchy_value();
    }
    void unlock() {
        this_thread_hierarchy_ = previous_hierarchy_;
        internal_.unlock();
    }
};

hierarchical_mutex high(10'000);
hierarchical_mutex mid(5'000);

int main() {
    std::lock_guard<hierarchical_mutex> h(high);
    std::lock_guard<hierarchical_mutex> m(mid);
    std::cout << "acquired in order\n";
    return 0;
}
