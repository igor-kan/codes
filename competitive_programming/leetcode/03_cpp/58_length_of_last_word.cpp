#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

int lengthOfLastWord(const std::string &text) {
    int length = 0, i = static_cast<int>(text.size()) - 1;
    while (i >= 0 && text[i] == ' ') --i;
    while (i >= 0 && text[i] != ' ') { ++length; --i; }
    return length;
}

int main() {
    assert(lengthOfLastWord("Hello World") == 5);
    assert(lengthOfLastWord("   fly me   to   the moon  ") == 4);
    std::cout << "58 length of last word ok\n";
    return 0;
}
