// Reverse a string in place.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>

void reverse_in_place(std::string &text) {
    std::size_t left = 0, right = text.size();
    while (left < right && left != --right) std::swap(text[left++], text[right]);
}

int main() {
    std::string text = "interview";
    reverse_in_place(text);
    assert(text == "weivretni");
    std::cout << text << '\n';
    return 0;
}
