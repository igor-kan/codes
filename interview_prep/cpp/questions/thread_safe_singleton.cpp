// Thread-safe singleton using function-local static (C++11 magic statics).
#include <iostream>
#include <mutex>
#include <thread>
#include <vector>

class Config {
  public:
    static Config &instance() {
        static Config config;  // initialized once, thread-safe
        return config;
    }
    int value() const { return value_; }
    void set(int value) { value_ = value; }
    Config(const Config &) = delete;
    Config &operator=(const Config &) = delete;

  private:
    Config() = default;
    int value_ = 0;
};

int main() {
    std::vector<std::thread> threads;
    for (int i = 0; i < 8; ++i)
        threads.emplace_back([] { Config::instance().set(42); });
    for (auto &t : threads) t.join();
    std::cout << "value=" << Config::instance().value() << '\n';
    return 0;
}
