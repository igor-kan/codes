// unique_ptr with a custom deleter and array specialization.
#include <cstdio>
#include <iostream>
#include <memory>

int main() {
    auto file = std::unique_ptr<std::FILE, int (*)(std::FILE *)>(
        std::fopen("smart_ptr_demo.txt", "w"), &std::fclose);
    if (file) std::fputs("owned by unique_ptr\n", file.get());

    auto buffer = std::make_unique<int[]>(4);
    for (int i = 0; i < 4; ++i) buffer[i] = i * i;

    std::cout << "buffer[3]=" << buffer[3] << '\n';
    return 0;
}
