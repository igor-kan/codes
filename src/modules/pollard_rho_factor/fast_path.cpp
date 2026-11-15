#include "interface.hpp"
namespace codes_pollard_rho_factor {
std::uint64_t strip_twos(std::uint64_t& n) {
    std::uint64_t cnt = 0;
    while (n > 0 && (n & 1ULL) == 0) { n >>= 1; cnt++; }
    return cnt;
}
} // namespace codes_pollard_rho_factor
