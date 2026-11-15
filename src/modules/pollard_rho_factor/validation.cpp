#include "interface.hpp"
namespace codes_pollard_rho_factor {
Status validate_n(std::uint64_t n) {
    return (n > 0) ? Status::Ok : Status::InvalidInput;
}
} // namespace codes_pollard_rho_factor
