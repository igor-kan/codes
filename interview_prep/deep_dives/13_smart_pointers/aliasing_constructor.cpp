// The aliasing constructor shares a control block but points at a subobject.
#include <iostream>
#include <memory>

struct Config {
    std::string name;
    int value;
};

int main() {
    auto config = std::make_shared<Config>(Config{"timeout", 30});
    std::shared_ptr<int> value_ptr(config, &config->value);  // aliasing
    std::cout << "count=" << value_ptr.use_count()
              << " value=" << *value_ptr << '\n';
    return 0;
}
