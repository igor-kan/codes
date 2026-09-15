// Constraining class templates and specializations.
#include <concepts>
#include <iostream>
#include <type_traits>

template <typename T>
struct Serializer {
    static std::string encode(T value) { return "int:" + std::to_string(value); }
};

template <typename T>
    requires std::floating_point<T>
struct Serializer<T> {
    static std::string encode(T value) { return "float:" + std::to_string(value); }
};

int main() {
    std::cout << Serializer<int>::encode(7) << ' '
              << Serializer<double>::encode(2.5) << '\n';
    return 0;
}
