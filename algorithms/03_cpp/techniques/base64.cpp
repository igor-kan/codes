// Base64 encoding.
#include <cassert>
#include <iostream>
#include <string>

std::string base64(const std::string &in) {
    static const char *B = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    std::string out;
    for (std::size_t i = 0; i < in.size(); i += 3) {
        unsigned v = static_cast<unsigned char>(in[i]) << 16;
        const int rem = static_cast<int>(in.size() - i);
        if (rem > 1) v |= static_cast<unsigned char>(in[i + 1]) << 8;
        if (rem > 2) v |= static_cast<unsigned char>(in[i + 2]);
        out.push_back(B[(v >> 18) & 63]);
        out.push_back(B[(v >> 12) & 63]);
        out.push_back(rem > 1 ? B[(v >> 6) & 63] : '=');
        out.push_back(rem > 2 ? B[v & 63] : '=');
    }
    return out;
}

int main() {
    assert(base64("foobar") == "Zm9vYmFy");
    assert(base64("f") == "Zg==");
    std::cout << "base64 ok\n";
    return 0;
}
