#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_manacher_palindrome_radii;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::string inp = "abacdfgdcabaaba";
    std::string pal = manacher_longest_palindrome(inp);
    std::string rev(pal.rbegin(), pal.rend());
    assert(pal == rev && pal.size() >= 3);
    return 0;
}
