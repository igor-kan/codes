// Check whether a string is a palindrome, ignoring non-alphanumerics.
#include <cassert>
#include <cctype>
#include <iostream>
#include <string>

bool is_palindrome(const std::string &text) {
    std::size_t left = 0, right = text.size();
    while (left < right) {
        while (left < right && !std::isalnum(static_cast<unsigned char>(text[left]))) ++left;
        while (left < right && !std::isalnum(static_cast<unsigned char>(text[--right])));
        if (left >= right) break;
        if (std::tolower(static_cast<unsigned char>(text[left])) !=
            std::tolower(static_cast<unsigned char>(text[right]))) return false;
        ++left;
    }
    return true;
}

int main() {
    assert(is_palindrome("A man, a plan, a canal: Panama"));
    assert(!is_palindrome("hello"));
    std::cout << "ok\n";
    return 0;
}
