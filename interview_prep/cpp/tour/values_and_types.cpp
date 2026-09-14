// A Tour of C++ -- values, types and initialization.
#include <cstdint>
#include <iostream>
#include <string>

int main() {
    int answer = 42;                        // direct initialization
    double pi{3.14159};                     // brace initialization (no narrowing)
    auto count = std::uint64_t{1'000'000};  // auto deduces unsigned long long
    std::string name = "C++";

    if (answer > 0 && !name.empty()) {
        std::cout << name << " " << answer << " pi=" << pi
                  << " count=" << count << '\n';
    }
    return 0;
}
