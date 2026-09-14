// Effective C++ -- perfect forwarding with universal references.
#include <iostream>
#include <string>
#include <utility>

struct Sink {
    void accept(int &) { std::cout << "lvalue int\n"; }
    void accept(int &&) { std::cout << "rvalue int\n"; }
    void accept(const std::string &) { std::cout << "string\n"; }
};

template <typename SinkT, typename... Args>
void dispatch(SinkT &sink, Args &&...args) {
    sink.accept(std::forward<Args>(args)...);
}

int main() {
    Sink sink;
    int value = 1;
    dispatch(sink, value);
    dispatch(sink, 2);
    dispatch(sink, std::string("text"));
    return 0;
}
