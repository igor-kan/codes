// Passing arguments by value, reference and move.
#include <functional>
#include <iostream>
#include <string>
#include <thread>

void by_value(std::string text) { std::cout << "value: " << text << '\n'; }
void by_reference(std::string &text) { text += "!"; }
void by_move(std::string text) { std::cout << "moved: " << text << '\n'; }

int main() {
    std::string shared = "shared";
    std::thread t1(by_value, shared);
    std::thread t2(by_reference, std::ref(shared));
    std::string owned = "owned";
    std::thread t3(by_move, std::move(owned));
    t1.join(); t2.join(); t3.join();
    std::cout << "after: " << shared << '\n';
    return 0;
}
